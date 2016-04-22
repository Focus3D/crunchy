# Introduction #

If you have reached this page, chances are that you are familiar with Google's Summer of Code (SoC).  Crunchy was largely born out of the Summer of Code in 2006 and has become an exciting collaboration.

Prior to submitting a proposal for working on Crunchy as a SoC project, you should have at least tried Crunchy.  We suggest that you go through the "Using Crunchy" tutorial (which should take less than 10 minutes) and perhaps the "Making Crunchy Tutorials" (how to...).

If you are adventurous, you might want to have a look at the existing code.


Currently, the unit test coverage for the Crunchy code is less than half done.  A SoC proposal may include a component dealing with improving the existing project by writing unit tests for it.

# Other SoC ideas #

The following are some ideas of varying complexity.  Some are suitable for a full project; others are shorter ones, doable in a few days by someone familiar with Crunchy and Python (and, possibly, a bit of Javascript):
  * Having the option to use unittest instead of doctest as an interactive element (would be a simple plugin, no more than 2 weeks). **Done**
  * Implement a Silverlight plugin for Crunchy.
  * Re-create Crunchy's functionality in Silverlight.
  * Session logging exists in a primitive form; extend them with possible automated emailing of log to teacher. Again should be only a subproject
  * Timed doctests (with the "Evaluate button" appearing only for a fixed amount of time) (should be a relatively simple change to the doctest plugin). This is also a short project. **Prototype exists**
  * Implementing rur-ple http://rur-ple.sf.net within Crunchy; this **might** be an ambitious SoC project.
  * Creating a new Crunchy version compatible with Python 3.0.  Some experimental work has been done showing that it should be doable in just a few weeks. **Almost completed**
  * Finding a way to stop an interpreter running thread.  This is apparently done by Sage, and would likely require the use of ctypes. **Done**
  * Creating a classroom server to keep track of student's responses to tests.
  * Create a collection of doctest-based problems for simple (and not so simple) Python exercises for list, strings, dicts, math functions, etc.  The beginning of a collection can be found at http://code.google.com/p/doctests/source/browse; this is the list referred to at http://wiki.python.org/moin/ProblemSets/99_Prolog_Problems_Solutions for problems 1 to 6.  **NOTE**: this, by itself, can not constitute a SoC project - they can not be simply tutorials.  But, if you develop further the doctest environment (by improving the logging, or adding a moinmoin plugin, or ...), then these could very well be integrated as test cases.
  * write twill scripts to do functional tests.
  * add a history to a Python interpreter so that commands previously typed in can be recalled by pressing the up arrow key.  (Note: this used to be part of Crunchy prior to version 0.8 - so it would just be a matter of retrieving the old [javascript](javascript.md) code and adapting it to the newer Crunchy.)
  * do live logging of Crunchy session accessible via a hackystat plugin.
  * incorporate pylint as an option to doctests so as to give an evaluation of the code "quality" at the same time as evaluating its correctness. **Done**
  * add a notebook (like Mathematica) feature for Crunchy where a user can create a simple tutorial inside a browser, with alternating text and Python code.

These are just some ideas; feel free to make your own suggestions!