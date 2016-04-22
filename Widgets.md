# Introduction #

I'm writing this mainly to test this wiki.

widgets.py contains classes that create the Crunchy Widgets as XHTML Trees.

All the widget classes implement `ElementTree._ElementInterface`. Widgets are created by
simply creating an instance of the appropriate class and appending the instance to the XML
tree.

The following widgets are (or will soon be) supported (parentheses are arguments to the
constructor:
  * `Interpreter(code)`
  * `Editor(buttons, code, rows=10, cols=80, copy=True, doctest=None)`
  * `ExecOutput`
  * `DoctestOutput`
  * `Canvas`
  * `Plot`
  * `Javascript`

In addition there are some constants:
  * `EXEC_BUTTON`
  * `DOCTEST_BUTTON`
  * `EXTERNAL_BUTTON`
  * `CONSOLE_BUTTON`