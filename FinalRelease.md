# Check list for an official release #

This document outlines the various checks that must be performed before an official release is made.  Some points mentioned here are specific to the final 1.0 release.

In some tables below, a release target version is listed.  This will always denote the latest (planned) release version for which the verification has been made.

## Issues ##

Resolve all relevant issues - all remaining open issues must have been tagged as being "beyond 1.0".  For releases beyond 1.0, we will have to update the tag as appropriate.

#### Useful lists of Issues: specific to 1.0 release ####
  * Open Release 1.0 issues: http://code.google.com/p/crunchy/issues/list?q=label%3AMilestone-Release1.0&can=2
  * Release 1.0 issues that need verification: http://code.google.com/p/crunchy/issues/list?can=7&q=label%3AMilestone-Release1.0&colspec=ID+Type+Status+Priority+Milestone+Owner+Summary&cells=tiles

Both of those lists should be empty.

## Appearance: specific to 1.0 release ##

Crunchy's "look" must have been finalized, with everyone (well... at least both Johannes
and André) agreeing about all styling issues.

## Testing ##

Ensure that Crunchy has been tested under
  1. At least one Linux flavor
  1. Windows
  1. Windows with path for user containing non-ascii character (André!)
  1. Mac OS

"Tested" means that Crunchy must have been run by a user, that all existing unit tests
have been executed as well as all the existing functional tests (using selenium).
This should be noted below, including the platform and the user.

#### Unit tests ####

As of May 2008, the unit test coverage is approximately half complete.  Normally, it is expected that unit tests will be run prior to each commit.  However, since development may be occuring only on one platform, it is important to verify that unit tests are working on all target platforms prior to a release.

| **Platform** | **Python version** | **Release target** | **Verified by**|
|:-------------|:-------------------|:-------------------|:---------------|
| Mac OS       |  2.4               | 0.9.9.3            | not ready yet  |
| Mac OS       |  2.5               | 0.9.9.3            |                |

#### Functional tests ####

Functional tests are run using selenium; see RunningSeleniumTests for details.

As of May 2008, the automated functional test coverage is less than 10% complete.  Still, it provides a very useful check.  Since development may be occuring only on one platform, it is important to verify that functional tests are performed on all target platforms prior to a release.

| **Platform** | **Python version** | **Release target** | **Verified by**|
|:-------------|:-------------------|:-------------------|:---------------|
| Mac OS       |  2.4               | 0.9.9.3            | not ready yet  |
| Mac OS       |  2.5               | 0.9.9.3            |                |

## Content ##

All html pages directly assessible from the left-hand-side menu must have been determined
to be completed.  Each of these should be noted below, indicating the page name and the
user who performed the official check.  **Note: this should be the very last thing done prior to a release, to ensure that the information is up to date and reflect all the changes made.  Do not update the table until then.**  A _bug fix_ release could be done without this QA check being made.

| **Page** | **Release target** | **Verified by**|
|:---------|:-------------------|:---------------|
| index.html |  0.9.9.3           | André          |
| crunchy\_tutor/welcome\_en.html |                    |                |
| crunchy\_tutor/interpreter\_en.html |                    |                |
| crunchy\_tutor/editor\_en.html |  0.9.9.3           | André          |
| crunchy\_tutor/doctest\_en.html |  0.9.9.3           | André          |
| crunchy\_tutor/canvas\_en.html |  0.9.9.3           |André           |
| crunchy\_tutor/images\_en.html |                    |                |
| crunchy\_tutor/external\_en.html |                    |                |
| crunchy\_tutor/remote\_en.html |                    |                |
| crunchy\_tutor/config\_en.html |                    |                |
| crunchy\_tutor/faq\_en.html |                    |                |
| crunchy\_tutor/writing\_en.html |                    |                |
| functional\_tests/index.html |                    |                |

Ensure that documentation is complete: for example, there is a simple turtle module included in the Crunchy distribution that should be documented.

#### Translations ####

Translations should be verified and, if possible, brought up to date.

| **Language** | **Release target** | **Status** | **Verified by** |
|:-------------|:-------------------|:-----------|:----------------|
| English      |                    |            |                 |
| French       |                    |            | André           |

To be completed later for the other 8 languages.

#### Included files ####

Try to make sure that included 3rd party code (e.g. editarea) are the latest version.

## Open issues ##

  * Should we remove all styling "hard-coded" information in .py files, like what was done when addressing [Issue 112](https://code.google.com/p/crunchy/issues/detail?id=112), prior to the 1.0 release?

## See also ##

  * BuildingReleases
  * [Issue 109](https://code.google.com/p/crunchy/issues/detail?id=109)