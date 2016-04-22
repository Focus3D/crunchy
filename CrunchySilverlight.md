# Introduction #

Microsoft Silverlight can run IronPython. This is a Good Thing. We would like to take advantage of this Good Thing!


# Taking advantage of a Good Thing #

Here is a list of the advantages that Silverlight can bring to Crunchy (please add our own ideas):
  * Using Silverlight we can execute code securely, in the browser - and it will be properly sandboxed.
  * It means that we wuld never have to write a single line in javascript again - we ca write it all in IronPython.
  * It makes the code run faster, because there is less overhead associated with setting up and tearing down IO connections.
  * If we do continue to communicate with the server, we can use a proper TCP connection - not some hacked layer on top of HTTP (yes, I mean you: COMET).
  * Better Graphics: we would have much more flexibility in terms of what we can draw (3D acceleration here we come...)
  * Easier to debug through VS (if you like that kind of thing) - thanks Amit
  * We can write unitests in python that run in the browser - see [Issue 103](https://code.google.com/p/crunchy/issues/detail?id=103) - actually, Selenium is a much better way of doing this.

Does anyone else have any ideas...?