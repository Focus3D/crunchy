# Introduction #

So, you are ready to start working on Crunchy development. Here's what you need to do to use the repository.

Important Legal Note: Crunchy is licensed under the MIT License. By submitting code to the Crunchy SVN repository (the repository), you implicitly license it under the MIT license (a sample copy of which is available at http://www.opensource.org/licenses/mit-license.php). You must own the copyright to any code you submit to the repository. Please ensure that you do not upload any code which you do not own. If you are unsure, then please contact either Johannes or André, who will advise you. In the event that you submit code to which you do not own the rights, it will be removed, and all write access to the repository will be revoked. You will retain the copyright to all original code that you submit to the repository. It is important to remember that if you are employed by a third party, then your employment agreement may give your employer rights to any works you produce - even in your own time, in your own home, on your own equipment - if you are in any doubt then please check with your employer.

It is important that you agree to these conditions before submitting code to the repository.

Less scary personal notice: Please, please, please make sure that you understand the previous two paragraphs. If you do not, then please contact André and/or Johannes and they will explain it all to you. Unlike some open-source projects, there is no single legal entity representing Crunchy. Legally, Crunchy is just an association of individuals. Please respect the rights of others. Any questions... please ask us...

# Accounts you will need #

You will need the following accounts/subscriptions (all require a google account):
  * An account on the Crunchy Google Code Project Site - email Johannes or André to get one.
  * We ask you to sign up to the crunchy-discuss and crunchy-notify maillinglists (links are on the front page)
  * You will need to know your google code SVN password (go to http://code.google.com/hosting/settings to find this)

# Now that you are all set, here's how to do it #

First of all, you need to know basic SVN. You can either use a command line client or a GUI (the svn integration into Eclipse is particularly good). If you haven't used SVN before, just google svn tutorial - there are plenty good ones out there.

## Committing to SVN ##

We ask that everyone commit stuff into their own branch - so before you start you will need to do an svn copy from the most up to date branch (it used to be André's, but it should be the trunk as of May 26 2008) to a new folder in the branches folder. Please name this folder something useful, like johannes or Muriel (i.e. use your own name!).

André and Johannes will take care of merging your branch into the trunk at regular intervals.

## Bugs and Clever Ideas ##

If you come across a bug, or have a clever idea, please create an issue for it in the issue tracker. Make sure you use sensible labels and if its a bug, please tell write down how to reproduce it. When you start working on an issue, please change the status to Started and when you are close an issue please mark it as Fixed. Never mark your own issues as Verified - let someone else come along and run tests - this is because two people are always better at testing than one!

# Things to do if you don't know what else to do... #

Here are a few of ideas (please add some more...):
  * Take a bug from the issue tracker and fix it
  * Write some tests
  * Take a bug from the tracker that has been marked as Fixed and test the hell out of it - if you are satisfied that it is indeed fixed, then mark the bug as Verified.