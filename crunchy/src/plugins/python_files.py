"""Plugin for loading and transforming python files."""

from src.interface import plugin, interactive, translate
from src.utilities import changeHTMLspecialCharacters, insert_file_browser
_ = translate['_']

def register():
    """Registers new http handler and new widget for loading ReST files"""
    plugin['register_http_handler']("/py", load_python)
    plugin['register_tag_handler']("span", "title", "load_python", insert_load_python)
    plugin['add_vlam_option']('power_browser', 'python')

class Python_file(object):
    """Simplest object that vlam will take as a file"""
    def __init__(self, data):
        self._data = data
    def read(self):
        '''
        return the only class attribute as a string; used to simulate a file
        '''
        return self._data

def load_python(request):
    """Loads python file from disk, inserts it into an html template
       and then creates new page
       """
    url = request.args["url"]
    # we may want to use urlopen for this?
    python_code = open(url).read()
    python_code = changeHTMLspecialCharacters(python_code)

    if interactive:
        interpreter_python_code = "__name__ = '__main__'\n" + python_code
    else:
        interpreter_python_code = python_code
    html_template = _("""
    <html>
    <head><title>%s</title></head>
    <body>
    <h1> %s </h1>
    <p>You can either use the interpreter to interact "live" with the
    Python file, or the editor.  To "feed" the file to the interpreter,
    first click on the editor icon next to it, and then click on the
    "Execute" button.
    <h3 > Using the interpreter </h3>
    <p>Click on the editor icon and feed the code to the interpreter.</p>
    <pre title="interpreter no_pre"> %s </pre>
     <h3 > Using the editor</h3>
    <pre title="editor"> %s </pre>

    </body>
    </html>
    """) % (url, url, interpreter_python_code, python_code)

    fake_file = Python_file(html_template)
    page = plugin['create_vlam_page'](fake_file, url, local=True)

    request.send_response(200)
    request.end_headers()
    request.wfile.write(page.read())

def insert_load_python(dummy_page, parent, dummy_uid):
    """Creates new widget for loading python files.
    Only include <span title="load_python"> </span>"""
    insert_file_browser(parent, 'Load local Python file', '/py')
    return
