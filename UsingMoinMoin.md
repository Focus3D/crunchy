# Using [MoinMoin](http://moinmo.in/) with Crunchy #

One exciting Crunchy forthcoming development is the integration with a Python-based wiki (MoinMoin) allowing collaborative work for Crunchy-aware tutorials.  Until this project is completed, you will have to install MoinMoin to experiment with this idea.

## Instructions ##

Go to [the MoinMoin Desktop Edition page](http://moinmo.in/DesktopEdition) and follow the instructions.  In particular, start MoinMoin (moin.py) locally.

Start Crunchy and go to the Browsing menu page.  Enter http://127.0.0.1:8080 as the URL for a remote tutorial and load it.  You may want to select **crunchy.no\_markup = 'interpreter'** using an interpreter prompt before loading this page.

Also, the security level for 127.0.0.1:8080 will be set to "display trusted" by default.  The "display" part means that no interaction will be permitted.  So, the security level will have to be changed (for example, via the menu - then reloading the page) before any interactivity can take place.

That's it.