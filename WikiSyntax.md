This page describe the wiki syntax which will be available to write tutorials.

# General wiki syntax #

For general elements, the wiki syntax will be the same as the [MoinMoin](http://moinmo.in/) one.
Read the [Syntax reference](http://moinmo.in/HelpOnMoinWikiSyntax).

The MoinMoin syntax is used because MoinMoin is the major wiki engine in the python world.

# Management of python code #

The most important change in the wiki syntax is the addition of a new "parser syntax" for VLAM <pre> markup, like (without spaces between bracket) this:<br>
<pre><code>{ { {#!crunchy vlam stuff<br>
 Python code<br>
} } }<br>
</code></pre>
where "vlam stuff" can be the same parameters than the one in the "title" attribute of <pre> markups in html.<br>
<br>
= Other VLAM makup =<br>
<br>
Some other VLAM makup like:<br>
* <a title="external_link" ...><br>
<br>
Unknown end tag for </a><br>
<br>
<br>
* <span title="load_local"> one or more spaces <br>
<br>
Unknown end tag for </span><br>
<br>
<br>
* <span title="load_remote"> optional url <br>
<br>
Unknown end tag for </span><br>
<br>
<br>
can be implemented through macros, like:<br>
* <<ExternalLink(url, name)>><br>
* <<LoadLocal>><br>
* <<LoadRemote(optional_url)>>