# Introduction #

By popular demand (André asked), here's how I got my mac set up for silverlight development.

Firstly, here is my computer setup - you may have problems if yours differs signifacantly from this:

  * OSX 10.5.2 (Leopard)
  * Camino Web browser (should work with anything based on webkit or gecko)


# How its done #

First you need to get silverlight 2.0: Go to http://dynamicsilverlight.net/ and hit _Download Now_ - make sure you get the mac version. Install this (run the .pkg file in the .dmg).

Next you need the Mono: go to http://www.go-mono.com/mono-downloads/download.html and get the mac version. You don't need to worry about the X11 warning at the bottom of the page - we won't be using mono for anything graphical. Go ahead and install this too.

Finally, you need to get the Dynamic Silverlight SDK from http://dynamicsilverlight.net/get/ - don't get the silverlight 2.0 SDK: it won't help you. This is a zip file, so go ahead and unzip it to your favourite directory.

Congratulations, you've installed Dynamic Silverlight on your mac.

# Quick and dirty getting started guide #

  1. Create a folder to hold your project
  1. Inside this folder create a another folder called app
  1. Inside this, create a file called app.py that will become the entrypoint of your application.
  1. Create an HTML file (in your project root directory, not the app directory) that has this inside it:
```
<object data="data:application/x-silverlight," type="application/x-silverlight-2-b1" width="0" height="0">
      <param name="source" value="app.xap"/>
      <param name="onerror" value="onSilverlightError" />
      <param name="background" value="white" />
      <param name="initParams" value="reportErrors=errorLocation" />
      <param name="windowless" value="true" />
      
      <a href="http://go.microsoft.com/fwlink/?LinkID=108182" style="text-decoration: none;">
          <img src="http://go.microsoft.com/fwlink/?LinkId=108181" alt="Get Microsoft Silverlight" style="border-style: none"/>
      </a>
</object>
```
  1. Write some code in app.py
  1. execute the following command (from within the project root) to build the .xap file:`mono <path to dynamic silverlight sdk>/bin/Chiron.exe /directory:app /zipdlr:app.xap`
  1. Open your HTML file and enjoy!

Note, the .xap file is how Silverlight applications are distributed.

Second note: Sorry if its a bit vague, I'm sitting on a freezing train station in Germany, waiting for a very delayed train.