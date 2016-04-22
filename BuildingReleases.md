# Getting the source into the right place #

First, you will need to copy the source code into a release tag in the SVN repository. You should do this using an SVN copy. If you are copying from the trunk then the command will look something like:
```
$ svn copy https://crunchy.googlecode.com/svn/trunk/crunchy/ https://crunchy.googlecode.com/svn/tags/version
```

where _version_ is the version number of the release you want to make (e.g. 0.9.9.3 or 1.0). You shouldn't create the tag until you are sure the release is ready for primetime. If you want to work on a release away from the trunk, then first copy it into a branch, and work on it there.

# Building the Release #

To build the release, you need an empty directory, I use a directory called temp\_release:
```
$ mkdir temp_release
```
Go into this directory (`cd temp_release`) and download the release script:
```
$ svn export http://crunchy.googlecode.com/svn/trunk/tools/build_release.py
```
This should download the script into the current directory, now all you have to do is run the script:
```
$ python build_release.py version zip tar.gz
```
again, replacing _version_ with the version number you used above. In this example I have told the script to build a zip file and a tar.gz file for distribution.

# What the Build Script Does #

The build script automatically exports the source code from SVN into a temporary directory. When this has finished, it tries to build all the targets that you have specified. You specify targets by listing them after the version.

## List of targets ##

| **Target** | **Description**                                             | **Notes** |
|:-----------|:------------------------------------------------------------|:----------|
| `zip`      | Creates a zip file (the traditional Crunchy distribution)   | runs on unix only |
| `tar.gz`   | Creates a tar.gz file, rather like the zip file above       | runs on unix only |
| `mac`      | Creates a mac .app using py2app                             | This only runs on OSX (and has only been tested on Leopard), buggy and needs polishing |
| `deb`      | Will create a .deb for Debian/Ubuntu users                  | Not implemented |
| `rpm`      | Will create a .rpm for Fedora/Redhat users                  | Not implemented |
| `py2exe`   | Will create a standalone .exe using py2exe                  | Not implemented |
| `nsis`     | Will create a Windows Installer using NSIS                  | Not implemented |
| `egg`      | Will create a Python egg                                    | Not implemented |
| `make`     | will create a tar.gz archive that can be installed by unarchiving, running configure, then make, then make install | Not implemented |