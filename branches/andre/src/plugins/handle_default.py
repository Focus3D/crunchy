"""This plugin handles loading all pages not loaded by other plugins"""

from imp import find_module
from os.path import normpath, join, isdir, dirname
from dircache import listdir, annotate
import sys

# All plugins should import the crunchy plugin API via interface.py
from src.interface import python_version, translate, plugin, server, debug, debug_msg

_ = translate['_']

def register():
    plugin['register_http_handler'](None, handler)

def path_to_filedata(path, root):
    """
    Given a path, finds the matching file and returns a read-only reference
    to it. If the path specifies a directory and does not have a trailing slash
    (ie. /example instead of /example/) this function will return none, the
    browser should then be redirected to the same path with a trailing /.
    Root is the fully qualified path to server root.
    Paths starting with / and containing .. will return an error message.
    POSIX version, should work in Windows.
    """
    if path == "/exit":
        server['server'].still_serving = False
        exit_file = join(root_path, "exit_en.html")
        return open(exit_file).read()
    if path.startswith("/") and (path.find("/../") != -1):
        return error_page(path)
    npath = normpath(join(root, normpath(path[1:])))

    if isdir(npath):
        if path[-1] != "/":
            return None
        else:
            return get_directory(npath)
    else:
        try:
            if npath.endswith(".html") or npath.endswith(".htm"):
                return plugin['create_vlam_page'](open(npath), path).read()
            # we need binary mode because otherwise the file may not get
            # read properly on windows (e.g. for image files)
            return open(npath, mode="rb").read()
        except IOError:
            try:
                return open(npath.encode(sys.getfilesystemencoding()),
                            mode="rb").read()
            except IOError:
                print("In path_to_filedata, can not open path = " + npath)
                return error_page(path)

def handler(request):
    """the actual handler"""
    if debug['handle_default'] or debug['handle_default.handler']:
        debug_msg("--> entering handler() in handle_default.py")
    data = path_to_filedata(request.path, root_path)
    if debug['handle_default'] or debug['handle_default.handler']:
        debug_msg("in handle_default.handler(), beginning of data =")
        try:
            d = data[0:80]
            if "\n" in d:
                d = d.split("\n")[0]
            debug_msg(d)
        except:
            debug_msg(data)
    if data == None:
        request.send_response(301)
        request.send_header("Location", request.path + "/")
        request.end_headers()
    else:
        request.send_response(200)
        request.end_headers()
        try:
            request.wfile.write(data)
        except:
            if python_version >=3:
                try:
                    data = bytes(data, sys.getdefaultencoding())
                except:
                    if debug['handle_default'] or debug['handle_default.handler']:
                        debug_msg("could not convert data to bytes")
                    else:
                        pass
                try:
                    request.wfile.write(data)
                except:
                    if debug['handle_default'] or debug['handle_default.handler']:
                        debug_msg("failed writing data in handler")
                    else:
                        pass

def get_directory(npath):
    _ = translate['_']
    childs = listdir(npath)
    annotate(npath, childs)
    for i in default_pages:
        if i in childs:
            return path_to_filedata("/"+i, npath)
    tstring = ""
    for child in childs:
        tstring += '<li><a href="' + str(child) + '">' + str(child) +'</a></li>'
    return dir_list_page % (_("Directory Listing"), tstring)

# the root of the server is in a separate directory:
root_path = join(plugin['get_root_dir'](), "server_root/")

default_pages = ["index.htm", "index.html"]

illegal_paths_page = """
<html>
<head>
<title>
%s <!--Illegal path, page not found. -->
</title>
</head>
<body>
<h1>%s<!--Illegal path, page not found. --></h1>
<p>%s <!--Crunchy could not open the page you requested. This could be for one of anumber of reasons, including: --></p>
<ul>
<li>%s <!--The page doesn't exist. --></li>
<li>%s<!--The path you requested was illegal, examples of illegal paths include those containg the .. path modifier.-->
</li>
</ul>
<p>%s <!--The path you requested was:--> <b>%s<!--path--></b></p>
</body>
</html>
"""

dir_list_page = """
<html>
<head>
<title>
%s
</title>
</head>
<body>
<ul>
<li><a href="../">..</a></li>
%s
</ul>
</body>
</html>
"""

def error_page(path):
    return illegal_paths_page % (_("Illegal path, page not found."), _("Illegal path, page not found."),
                                 _("Crunchy could not open the page you requested. This could be for one of anumber of reasons, including:"),
                                 _("The page doesn't exist."),
                                 _("The path you requested was illegal, examples of illegal paths include those containing the .. path modifier."),
                                 _("The path you requested was: "),
                                 path)
