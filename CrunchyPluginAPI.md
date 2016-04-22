Documentation for the Crunchy Plugin API

# Introduction #

Starting with version 0.8, Crunchy has been redesigned to be extensible via plugins.  Many of Crunchy's functions have been re-written as plugins.

In order to allow isolated testing of individual plugins, a special module (interface.py) has been defined as a bridge between Crunchy's core and plugins.

The following document provides a quick overview of Crunchy's plugin API.

## What is a plugin? ##

A plugin is a .py file in the plugins directory which contains at least a register() function. A plugin can optionally specify a set of services it provides and another set of services that it requires. Plugins will be registered in an order that guarantees all required services to be available at registration time.

### Contents of a plugin module ###

There are only three elements of a plugin module specified by the API:
  * `register()` is a function used to register the plugin. Plugins should not perform any initialisation until this is called and all services specified in `provides` must be available after this is called.
  * `requires` is a set of services required by this plugin.
  * `provides` is another set of services that this plugin provides.

Example plugin file:
```
# import the API:
from src.interface import plugin

provides = set(["http_hello"])
requires = set()

def register():
    """Go ahead and register the plugin"""
    plugin['register_http_handler'](None, hello_handler)
    
...
```
# The `CrunchyPlugin` Module #

This contains virtually all of the API.


The `CrunchyPlugin`, which module provides the following functions:

## register\_http\_handler(pattern, handler) ##

Used to register a custom handler for an http path.

If `pattern` is `None` then handler will be registered as the default handler (which handles all otherwise unmatched paths). Otherwise `pattern` should be a string containing the path to match.

`handler` should be a callable object that takes one argument: A CrunchyRequest object (see below).

```
def register():
    register_http_handler("/mypath", mypath_handler)
    
def mypath_handler(request):
    print "handling /mypage"
```

## register\_tag\_handler(tag, attribute, keyword, handler) ##

Used to register a custom handler for an html element.

`tag`, `attribute` and `keyword` should be Strings. `tag` and `attribute` are the normal html tag and attribute whereas `keyword` is taken to be the first "word" in the attribute string. For example, in <pre title='interpreter linenumber'>, pre is the tag, title is the attribute, and interpreter would be the keyword.<br>
<br>
<br>
handler should be a callable object that takes three arguments: A CrunchyPage object (see below), an elementtree.Element object and a unique string ID (uid).<br>
<br>
Example:<br>
<pre><code>def register(self):<br>
    plugin['register_tag_handler']("pre", "title", "editor", insert_editor)<br>
    <br>
def insert_editor(page, elem, uid):<br>
    print "inserting an editor..."<br>
</code></pre>

=*The following needs to be updated*=<br>
== create_vlam_page(filehandle) ==<br>
<br>
Creates (and returns) a CrunchyPage object from filehandle. CrunchyPage objects should not be created directly but via this factory function.<br>
<br>
Basically this is used to kick-start the parsing of a VLAM file.<br>
<br>
== exec_code(uid) ==<br>
<br>
Executes some code in a new thread. Uses uid as the IO redirection ID (see CrunchyCommunication).<br>
<br>
== register_service(function, servicename) ==<br>
<br>
Creates a new service. Services are functions accessible from all plugins as CrunchyPlugins.services.servicename().<br>
<br>
function should be a callable object.<br>
<br>
Example:<br>
<pre><code>def register():<br>
    register_service(test_service)<br>
    register_http_handler("/service_test", test_http)<br>
    <br>
def test_http(rq):<br>
    rq.send_response(200)<br>
    rq.end_headers()<br>
    rq.wfile.write(services.test_service({"test_key_1":1}))<br>
    <br>
def test_service(arg):<br>
    return str(arg)<br>
</code></pre>

== exec_js(pageid, code) ==<br>
<br>
Executes some javascript code in the page referred to by pageid.<br>
<br>
Example:<br>
<pre><code>exec_js(pageid, 'alert("Hello World");')<br>
</code></pre>
This example will display a "Hello World" message box to the user.<br>
<br>
= CrunchyRequest =<br>
<br>
This is the object passed to custom http handlers (see above).<br>
<br>
For now this is more or less a SimpleHTTPRequestHandler object, but in future it will become more customised and deveoper friendly.<br>
<br>
#todo: design a proper API for this<br>
<br>
Here are some instance variables:<br>
<br>
== path ==<br>
<br>
A String containing the path of the http request.<br>
<br>
== args ==<br>
<br>
A dict containing any arguments that were encoded in the URL.<br>
<br>
== data ==<br>
<br>
A string containing any data sent in the body of the request, only really relevant to POST requests.<br>
<br>
And some useful methods:<br>
<br>
== send_response(code) ==<br>
<br>
Begins an HTTP response. Sends off the code as the HTTP response code.<br>
<br>
== end_headers() ==<br>
<br>
Ends the HTTP header block and readies the connection for data to be sent.<br>
<br>
== wfile.write(data) ==<br>
<br>
Writes data to the connection.<br>
<br>
*Note:* This will definately change in future to just write() or write_data().<br>
<br>
Example:<br>
<pre><code>def custom_http_handler(request):<br>
    print request.path<br>
    request.send_respoonse(200)<br>
    request.end_headers()<br>
    request.wfile.write("Hello!")<br>
</code></pre>

= CrunchyPage =<br>
<br>
This is the object used to parse and store the state of a VLAM page.<br>
<br>
It is currently not at all developer friendly or documentable (I'm still in the process of moving stuff out of here and into plugins).<br>
<br>
#todo: get a proper API in here too.