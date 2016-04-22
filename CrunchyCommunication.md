An overview of the new COMET based communication framework for crunchy.  **Note that this is not yet implemented in the public 0.8a release.**

# Introduction #

Crunchy uses a highly customised HTTP Server to display its content. Using a bit of JavaScript on the Client page, this server is capable of sending data to the client without the client polling. This results in much higher responsiveness with much reduced resource usage.

The core of Crunchy is an HTTP Server that spawns a new thread for each request. Requests are handled by registering custom handler callbacks with the server. These are python functions that take only one argument, a reference to a CrunchyHTTPRequest object.

This document will assume that a HTTPServer called `server` is running.

## The Server's Request Callback API ##

Here is an example handler function:

```
def hello_handler(request):
    request.send_response(200)
    request.end_headers()
    request.wfile.write("Hello World!")
```

to register this handler for the **/helloworld** page one would then call

```
server.register_handler(hello_handler, "/helloworld")`
```

From then on, whenever the **/helloworld** page is requested, the string `"Hello World"` will be sent to the server.

The CrunchyHTTPRequest objects have the following methods and attributes:

  * **send\_response(response\_code)**
> > Begins a HTTP response. The most useful response codes are 200 (OK), 404 (File not Found) and 500 (Internal Server Error) (see http://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html#sec6.1.1)
  * **end\_headers()**
> > Ends the HTTP header block. Once this has been called, data can be written to the client.
  * **wfile**
> > A writeable file-like object. Call its write() method to send data to the client.
  * **args**
> > A dictionary of URL-encoded arguments passed in the request. For example the URL **/example?arg1=val1&arg2=val2** would result in an args attrubute of `{"arg1":"val1", "arg2":"val2"}`
  * **data**
> > The data contained within the HTTP Request. This is really only meaningful for POST requests - but using XMLHttpRequest.send() it is conceivable that data could be sent for any request method.
  * **server**
> > This is simply a reference to the HTTPServer object that spawned the request.

## Some Custom Methods ##

Crunchy uses two custom urls for internal communication: **/comet** for server->client and **/post** for client->server.

### /post ###

This is very simple - it is opened as a POST method, with just one argument (**uid**)  to indicate which element the data is coming from. The data for the request is embedded in the body.

**Example request:**
```
POST /post?uid=1 HTTP/1.1

test data
```
**And response**:
```
HTTP/1.0 200 (OK)
```
(And yes, the response is correct, because Crunchy uses only HTTP/1.0)

### /comet ###

This is used for communication from the server. The client opens a **/comet** request and the server responds when there is data to be sent. When the client has received a response it immediately opens a new request which will hang until the server responds and so on...

**/comet** requests should specify a unique page id when they are fired off. ie. the full path will be something like: **/comet?page=0**. This is to facilitate multiple pages connecting. These unique IDs are acquired by a call to /page\_init.

The responses to **/comet** have a specific form. A complete response looks like:
```
Response = Response-Type SP Channel-Id CR Data

Response-Type = "STDOUT" | "STDERR" | "STOP" | "RESET"
```
where `Channel` is some integer (as a string) and `Data` is the response data.

Future additions to response types will include `"JSCODE"` (for the canvas) and `"POPUP"` for notifications of error states in Crunchy (although of course there won't be any).

The meanings of the response types are as follows:
  * **STDOUT**: data is raw (standard) output to be appended to the output of the IO elemnt denoted by Channel-Id.
  * **STDERR**: Is similar, but for stderr output.
  * **STOP**: Indicates that ouput has ended, tells the client to disable input for that element.
  * **RESET**: tells the client to reset the given IO Element.
  * **JSCODE**: Will execute the given Javascript code within the page.
  * **POPUP**: Will display a popup (possibly just using alert()) to give status information to the user. **Not Implemented**