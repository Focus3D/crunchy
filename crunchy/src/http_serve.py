"""
serve HTTP in a beautiful threaded way, allowing requests to branch
off into new threads and handling URL's automagically
This was built for Crunchy - and it rocks!
In some ways it is more restrictive than the default python HTTPserver -
for instance, it can only handle GET and POST requests and actually
treats them the same.
"""

from SocketServer import ThreadingMixIn, TCPServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib,urllib2
from traceback import format_exc
import base64,md5
import time
from src.interface import python_version, python_minor_version
from src.utilities import uidgen
import src.CrunchyPlugin as CrunchyPlugin

DEBUG = False

# FIXME: where should this dictionarry be put (instead of being blobal for
# the module?
users = {"crunchy" : "password"}

def require_basic_authenticate(func):
    '''A decorate  to addd  basic http authorization check to HTTP Request Handlers'''
    def wrapped(self):
        #if not hasattr(self, 'need_authenticated'):
        #    return func(self)
        if not hasattr(self, 'authenticated'):
            self.authenticated = False
        if not self.authenticated and 'Authorization' in self.headers:
            auth_word = self.headers['Authorization'].split()
            if auth_word[0] != 'Basic':
                self.authenticated = False 
            elif len(auth_word) > 1:
                user,password = base64.b64decode(auth_word[1]).split(':')
                if user == 'crunchy' and password == 'crunchypassword':
                    self.authenticated = True
        if not self.authenticated:
            self.send_response(401)
            self.send_header('WWW-Authenticate','Basic realm="Crunchy Access"')
            self.end_headers()
            self.wfile.write("You are not allowed to access this page.") 
    return wrapped

def require_digest_access_authenticate(func):
    '''A decorate  to addd  deigest authorization check to HTTP Request Handlers'''
    #TODO:Find a bettter way to decide what method we are dealing with ..
    if "GET" in func.__name__:
        method = "GET"
    else:
        method = "POST"
    realm = "Crunchy Access"

    def wrapped(self):
        #if not hasattr(self, 'need_authenticated'):
        #    return func(self)
        md5hex = lambda x:md5.md5(x).hexdigest()

        if not hasattr(self, 'authenticated'):
            self.authenticated =  None
        auth = self.headers.getheader('authorization')
        if not self.authenticated and auth is not None:
            token, fields = auth.split(' ', 1)
            if token == 'Digest':
                cred = urllib2.parse_http_list(fields)
                cred = urllib2.parse_keqv_list(cred)
                if 'realm' not in cred or 'username' not in cred \
                    or 'nonce' not in cred or 'uri' not in cred or 'response' not in cred:
                    self.authenticated = False
                elif cred['realm'] != realm or cred['username'] not in users:
                    self.authenticated = False
                elif 'qop' in cred and ('nc' not in cred or 'cnonce' not in cred): 
                    self.authenticated = False
                else:
                    if 'qop' in cred:
                        expect_response = md5hex('%s:%s'%( 
                            md5hex('%s:%s:%s' %(cred['username'], realm , users.get(cred['username'], ""))),
                            ':'.join([cred['nonce'],cred['nc'],cred['cnonce'],cred['qop'], md5hex('%s:%s' %(method, self.path))])
                            )
                        )
                    else:
                        expect_response = md5hex('%s:%s' %(
                            md5hex('%s:%s:%s' %(cred['username'], realm , users.get(cred['username'], ""))),
                            ':'.join([cred['nonce'], md5hex('%s:%s' %(method, self.path))])
                            )
                        )
                    self.authenticated = (expect_response == cred['response'])

        if self.authenticated is None:
            msg = "You are not allowed to access this page.Please login first!"
        elif self.authenticated is False:
            msg = "Authenticated Failed"

        if  not self.authenticated :
            self.send_response(401)
            self._nonce = md5hex("%d:%s" % (time.time(), realm))
            self.send_header('WWW-Authenticate','Digest realm="%s", qop="auth", algorithm="MD5", nonce="%s"' %(realm, self._nonce))
            self.end_headers()
            self.wfile.write(msg) 
        else:
            return func(self)

    return wrapped

class MyHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    def __init__(self, addr, rqh):
        self.default_handler = None
        self.handler_table = {}
        HTTPServer.__init__(self, addr, rqh)

    def register_default_handler(self, handler):
        """register a default handler"""
        self.default_handler = handler

    def register_handler(self, path, handler):
        """
        register a handler function
        the function should be of the form: handler(request)
        """
        self.handler_table[path] = handler

    def register_handler_instance(self, handlerinstance):
        """register a handler class instance,
        the instance functions should be of the form: class.handler(self, request)
        and should have as their docstring the path they want to handle
        """
        pass

    def get_handler(self, path):
        """returns none if no handler registered"""
        if DEBUG:
            print("entering get_handler")
        if path in self.handler_table:
            return self.handler_table[path]
        else:
            return self.default_handler

class HTTPRequestHandler(BaseHTTPRequestHandler):

    #@require_basic_authenticate
    @require_digest_access_authenticate
    def do_POST(self):
        """handle an HTTP request"""
        # at first, assume that the given path is the actual path and there are no arguments
        realpath = self.path
        if python_version >=3:
            realpath = str(realpath)
        if DEBUG:
            print(realpath)
        argstring = ""
        self.args = {}
        # if there is a ? in the path then there are some arguments, extract them and set the path
        # to what it should be
        if self.path.find("?") > -1:
            realpath, argstring = self.path.split("?")
        self.path = urllib.unquote(realpath)
        if realpath.startswith("/generated_image"):
            realpath = "/generated_image"
            self.path = "/generated_image"
        # parse any arguments there might be
        if argstring:
            arg = []
            arglist = argstring.split('&')
            for i in arglist:
                arg = i.split('=')
                val = ''
                if len(arg) > 1:
                    self.args[arg[0]] = urllib.unquote_plus(arg[1])
        # extract any POSTDATA
        self.data = ""
        if "Content-Length" in self.headers:
            self.data = self.rfile.read(int(self.headers["Content-Length"]))
        # and run the handler
        if DEBUG:
            print("preparing to call get_handler in do_POST")
        try:
            self.server.get_handler(realpath)(self)
        except:
            # if there is an error, say so
            if python_minor_version == 'a2':
                print('problem found in do_POST')
                print('self.data = ' + str(self.data))
                print('realpath = ' + str(realpath))
            self.send_response(500)
            self.end_headers()
            self.wfile.write(format_exc())

##        if CrunchyPlugin.server.still_serving == False:
##            #sometimes the program does not exit; so force it...
##            import sys
##            sys.exit()

    #@require_basic_authenticate
    @require_digest_access_authenticate
    def do_GET(self):
        """the same as POST, we draw no distinction"""
        self.do_POST()

    def send_response(self, code):
        BaseHTTPRequestHandler.send_response(self, code)
        self.send_header("Connection", "close")


