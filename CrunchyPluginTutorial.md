Tutorial for the Crunchy Plugin System **Note: This does not apply to the current 0.8a release**

Updated 4 March '07

# The Crunchy Architecture #

Crunchy has a two-tier architecture, it is a set of plugins running on a core which provides certain basic services.

## Services ##

The following basic services are supplied by the Crunchy core:

  * VLAM Parsing
  * HTTP Serving
  * AJAX/COMET based communication with the page
  * Code execution (with a matching IO widget for the UI)

# The Plugin API #

I'm going to write this in the form of a tutorial, For the Documentation please look at CrunchyPluginAPI. The code for all these examples is included in the Crunchy distribution under `src/plugins/testplugins.py` (in fact we are reconstructing some of the test cases here).

## A Very Simple Plugin (VSP) ##

Plugins are classes that inherit `CrunchyPlugin`. These classes must be defined in .py files in the `plugins/` sudirectory.

First, create a new file in the plugins/ subdirectory called `tuteplugin.py`. This is going to contain all our tutorial plugins. We also need to edit crunchy.py to load this file (Note: this requirement will disappear soon): edit the call to `init_plugin_system()`, adding the string `"tuteplugin"` to the list of plugins. Your plugin is now registered.

Now we can start to create the plugin itself, open up tuteplugin.py and import the Plugin API like so:
```
from CrunchyPlugin import CrunchyPlugin
```

This imports the `CrunchyPlugin` class that is the basis of all plugins. A plugin is created by simply subclassing `CrunchyPlugin` and overriding the `register()` method:
```
class VSP(CrunchyPlugin):
    def register(self):
        pass
```

Wunderbar, you've just created a very simple dummy plugin. If you start Crunchy now then this will be loaded (although it won't actually do anything just yet). Basically, when Crunchy starts it will create an instance of your plugin class and call its `register()` method. The register method performs much the same function that `__init__()` does in a normal class, but you must **never** override `__init__()` method becuase the `__init__()` method of `CrunchyPlugin` does some vital general plugin setup (including calling your `register()` method).

Just so we can see it do something, change the `register()` method to read
```
def register(self):
    print "A very simple plugin is loading..."
```

## Making it do something ##

Now we want our plugin to do something useful... The simplest part of the API is the custom HTTP handling section. We are going to create a custom "/hello" page.

Go ahead and create a new plugin class:
```
class HelloHTTP(CruchyPlugin):
```

We need to create a custom http request handling method:
```
    def hello_handler(self, request):
        request.send_response(200)
        request.end_headers()
        request.wfile.write("Hello World!")
```

and a new register method:
```
    def register(self):
        self.register_http_handler("/hello", self.hello_handler)
```

Now if you run crunchy and visit the "/hello" page, you should be suitably greeted.

## TODO ##

  * describe vlam handlers
  * describe vlam creation
  * describe execution