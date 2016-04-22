# Introduction #

This sub-project started out as [issue 122](https://code.google.com/p/crunchy/issues/detail?id=122). It is now tracked in the better\_javascript branch. Hopefully, by using a modern Javascript library like jQuery or Mochikit we can make crunchy more responsive, more reliable, more cross-platform and generally prettier (see, for example, [issue 124](https://code.google.com/p/crunchy/issues/detail?id=124)).

## Notes ##

I will track progress in the comments to [issue 122](https://code.google.com/p/crunchy/issues/detail?id=122), and I will document work done on this page.

# Changelog #

_2008-06-02_ I have decided to initially focus on jQuery. I have created the better\_javascript branch in the repository, and will be using it for updates.

_2008-06-02_ I have vlam.py so that the COMET call is run using jQuery. this should solve 9/10ths of our problems with IE. See [revision 719](https://code.google.com/p/crunchy/source/detail?r=719) for more details.

_2008-06-02_ In [revision 721](https://code.google.com/p/crunchy/source/detail?r=721) I have over the output system to jQuery. This means that all of the javascript in cometIO.py has been converted.

_2008-06-03_ Widget uids are now separated by underscores instead of colons. This is because jQuery selectors have trouble with colons.