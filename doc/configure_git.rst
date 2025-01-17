:orphan:

.. include:: links.inc

.. _using_github:

Using GitHub to make a Pull Request
===================================

Any contributions to MNE, whether bug fixes,
improvements to the documentation, or new functionality, can be done via
*pull requests* on GitHub. The workflow for this is described here.
[Many thanks to Astropy_ for providing clear instructions that we have
adapted for our use here!]

The only absolutely necessary configuration step is identifying yourself and
your contact info:

.. code-block:: bash

   $ git config --global user.name "Your Name"
   $ git config --global user.email you@yourdomain.example.com

If you are going to :ref:`setup-github` eventually, this email address should
be the same as the one used to sign up for a GitHub account. For more
information about configuring your git installation, see :ref:`customizing-git`.

The following sections cover the installation of the git software, the basic
configuration, and links to resources to learn more about using git.
However, you can also directly go to the `GitHub help pages
<https://help.github.com/>`_ which offer a great introduction to git and
GitHub.

In the present document, we refer to the ``mne-python/master`` branch, as the
*trunk*.

.. _forking:

Creating a fork
^^^^^^^^^^^^^^^

You need to do this only once for each package you want to contribute to. The
instructions here are very similar to the instructions at
https://help.github.com/fork-a-repo/ -- please see that page for more
details. We're repeating some of it here just to give the specifics for the
mne-python_ project, and to suggest some default names.

.. _setup-github:

Set up and configure a GitHub account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't have a GitHub account, go to the GitHub page, and make one.

You then need to configure your account to allow write access -- see
the *Generating SSH keys* help on `GitHub Help`_.

Create your own fork of a repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you should fork the core ``mne-python.git`` repository:

#. Log into your GitHub account.

#. Go to the `mne-python GitHub`_ home.

#. Click on the *fork* button:

   .. image:: _static/forking_button.png

   Now, after a short pause and some 'Hardcore forking action', you should
   find yourself at the home page for your own forked copy of mne-python_.

Setting up the fork and the working directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Briefly, this is done using:

.. code-block:: bash

   $ git clone git@github.com:your-user-name/mne-python.git
   $ cd mne-python
   $ git remote add upstream git://github.com/mne-tools/mne-python.git

These steps can be broken out to be more explicit as:

#. Clone your fork to the local computer:

   .. code-block:: bash

      $ git clone git@github.com:your-user-name/mne-python.git

#. Change directory to your new repo:

   .. code-block:: bash

      $ cd mne-python

   Then type:

   .. code-block:: bash

      $ git branch -a

   to show you all branches.  You'll get something like::

    * master
    remotes/origin/master

   This tells you that you are currently on the ``master`` branch, and
   that you also have a ``remote`` connection to ``origin/master``.
   What remote repository is ``remote/origin``? Try ``git remote -v`` to
   see the URLs for the remote.  They will point to your GitHub fork.

   Now you want to connect to the mne-python repository, so you can
   merge in changes from the trunk:

   .. code-block:: bash

      $ cd mne-python
      $ git remote add upstream git://github.com/mne-tools/mne-python.git

   ``upstream`` here is just the arbitrary name we're using to refer to the
   main mne-python_ repository.

   Note that we've used ``git://`` for the URL rather than ``git@``. The
   ``git://`` URL is read only. This means we that we can't accidentally (or
   deliberately) write to the upstream repo, and we are only going to use it
   to merge into our own code.

   Just for your own satisfaction, show yourself that you now have a new
   'remote', with ``git remote -v show``, giving you something like::

       upstream   git://github.com/mne-tools/mne-python.git (fetch)
       upstream   git://github.com/mne-tools/mne-python.git (push)
       origin     git@github.com:your-user-name/mne-python.git (fetch)
       origin     git@github.com:your-user-name/mne-python.git (push)

   Your fork is now set up correctly.

#. Install mne with editing permissions using the installed folder:

   To be able to conveniently edit your files after installing mne,
   install using the following setting:

   .. code-block:: bash

      $ python setup.py develop --user

   To make changes in the code, edit the relevant files and restart the
   ipython kernel for changes to take effect.

#. Ensure unit tests pass

   Make sure before starting to code that all unit tests pass with `pytest`_:

   .. code-block:: bash

      $ make test

   That's it! You are now ready to hack away.

Workflow summary
----------------

This section gives a summary of the workflow once you have successfully forked
the repository, and details are given for each of these steps in the following
sections.

* Don't use your ``master`` branch for anything.  Consider deleting it.

* When you are starting a new set of changes, fetch any changes from the
  trunk, and start a new *feature branch* from that.

* Make a new branch for each separable set of changes -- "one task, one
  branch" (`ipython git workflow`_).

* Name your branch for the purpose of the changes - e.g.
  ``bugfix-for-issue-14`` or ``refactor-database-code``.

* If you can possibly avoid it, avoid merging trunk or any other branches into
  your feature branch while you are working.

* If you do find yourself merging from the trunk, consider :ref:`rebase-on-trunk`

* **Ensure all tests still pass**. Make `travis`_ happy.

* Ask for code review!

This way of working helps to keep work well organized, with readable history.
This in turn makes it easier for project maintainers (that might be you) to
see what you've done, and why you did it.

See `linux git workflow`_ and `ipython git workflow`_ for some explanation.

Deleting your master branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^

It may sound strange, but deleting your own ``master`` branch can help reduce
confusion about which branch you are on.  See `deleting master on github`_ for
details.

.. _update-mirror-trunk:

Updating the mirror of trunk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From time to time you should fetch the upstream (trunk) changes from GitHub:

.. code-block:: bash

   $ git fetch upstream

This will pull down any commits you don't have, and set the remote branches to
point to the right commit. For example, 'trunk' is the branch referred to by
(remote/branchname) ``upstream/master`` - and if there have been commits since
you last checked, ``upstream/master`` will change after you do the fetch.

.. _make-feature-branch:

Making a new feature branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you are ready to make some changes to the code, you should start a new
branch. Branches that are for a collection of related edits are often called
'feature branches'.

Making an new branch for each set of related changes will make it easier for
someone reviewing your branch to see what you are doing.

Choose an informative name for the branch to remind yourself and the rest of
us what the changes in the branch are for. For example ``add-ability-to-fly``,
or ``buxfix-for-issue-42``.

.. code-block:: bash

   # Update the mirror of trunk
   $ git fetch upstream

   # Make new feature branch starting at current trunk
   $ git branch my-new-feature upstream/master
   $ git checkout my-new-feature

Generally, you will want to keep your feature branches on your public GitHub_
fork. To do this, you `git push`_ this new branch up to your
github repo. Generally (if you followed the instructions in these pages, and
by default), git will have a link to your GitHub repo, called ``origin``. You
push up to your own repo on GitHub with:

.. code-block:: bash

   $ git push origin my-new-feature

In git > 1.7 you can ensure that the link is correctly set by using the
``--set-upstream`` option:

.. code-block:: bash

   $ git push --set-upstream origin my-new-feature

From now on git will know that ``my-new-feature`` is related to the
``my-new-feature`` branch in the GitHub repo.

.. _edit-flow:

The editing workflow
--------------------

Overview
^^^^^^^^

.. code-block:: bash

   $ git add my_new_file
   $ git commit -am 'FIX: some message'
   $ git push

In more detail
^^^^^^^^^^^^^^

#. Make some changes

#. See which files have changed with ``git status`` (see `git status`_).
   You'll see a listing like this one::

     # On branch ny-new-feature
     # Changed but not updated:
     #   (use "git add <file>..." to update what will be committed)
     #   (use "git checkout -- <file>..." to discard changes in working directory)
     #
     #    modified:   README
     #
     # Untracked files:
     #   (use "git add <file>..." to include in what will be committed)
     #
     #    INSTALL
     no changes added to commit (use "git add" and/or "git commit -a")

#. Check what the actual changes are with ``git diff`` (`git diff`_).

#. Add any new files to version control ``git add new_file_name`` (see
   `git add`_).

#. Add any modified files that you want to commit using
   ``git add modified_file_name``  (see `git add`_).

#. Once you are ready to commit, check with ``git status`` which files are
   about to be committed::

    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #    modified:   README

   Then use ``git commit -m 'A commit message'``. The ``m`` flag just
   signals that you're going to type a message on the command line. The `git
   commit`_ manual page might also be useful.

   It is also good practice to prefix commits with the type of change, such as
   ``FIX:``, ``STY:``, or ``ENH:`` for fixes, style changes, or enhancements.

#. To push the changes up to your forked repo on GitHub, do a ``git
   push`` (see `git push`_).

Asking for your changes to be reviewed or merged
------------------------------------------------

When you are ready to ask for someone to review your code and consider a merge:

#. Go to the URL of your forked repo, say
   ``https://github.com/your-user-name/mne-python``.

#. Use the 'Switch Branches' dropdown menu near the top left of the page to
   select the branch with your changes:

   .. image:: _static/branch_dropdown.png

#. Click on the 'Pull request' button:

   .. image:: _static/pull_button.png

   Enter a title for the set of changes, and some explanation of what you've
   done. Say if there is anything you'd like particular attention for - like a
   complicated change or some code you are not happy with.

   If you don't think your request is ready to be merged, prefix ``WIP:`` to
   the title of the pull request, and note it also in your pull request
   message. This is still a good way of getting some preliminary code review.
   Submitting a pull request early on in feature development can save a great
   deal of time for you, as the code maintainers may have "suggestions" about
   how the code should be written (features, style, etc.) that are easier to
   implement from the start.

#. Finally, make `travis`_ happy. Ensure that builds in all four jobs pass. To make code python3 compatible, refer to ``externals/six.py``. Use virtual environments to test code on different python versions. Please remember that `travis`_ only runs a subset of the tests and is thus not a substitute for running the entire test suite locally.

#. For the code to be mergeable, please rebase w.r.t master branch.

#. Once, you are ready, prefix ``MRG:`` to the title of the pull request to indicate that you are ready for the pull request to be merged.


If you are uncertain about what would or would not be appropriate to contribute
to MNE, don't hesitate to either send a pull request, or open an issue
on the mne-python_ GitHub site to discuss potential changes.

.. _rebase-on-trunk:

Rebasing on trunk
^^^^^^^^^^^^^^^^^

Let's say you thought of some work you'd like to do. You
:ref:`update-mirror-trunk` and :ref:`make-feature-branch` called
``cool-feature``. At this stage trunk is at some commit, let's call it E. Now
you make some new commits on your ``cool-feature`` branch, let's call them A,
B, C. Maybe your changes take a while, or you come back to them after a while.
In the meantime, trunk has progressed from commit E to commit (say) G::

          A---B---C cool-feature
         /
    D---E---F---G trunk

At this stage you consider merging trunk into your feature branch, and you
remember that this here page sternly advises you not to do that, because the
history will get messy. Most of the time you can just ask for a review, and
not worry that trunk has got a little ahead. But sometimes, the changes in
trunk might affect your changes, and you need to harmonize them. In this
situation you may prefer to do a rebase.

Rebase takes your changes (A, B, C) and replays them as if they had been made
to the current state of ``trunk``. In other words, in this case, it takes the
changes represented by A, B, C and replays them on top of G. After the rebase,
your history will look like this::

                  A'--B'--C' cool-feature
                 /
    D---E---F---G trunk

See `rebase without tears`_ for more detail.

To do a rebase on trunk:

.. code-block:: bash

    # Update the mirror of trunk
    $ git fetch upstream

    # Go to the feature branch
    $ git checkout cool-feature

    # Make a backup in case you mess up
    $ git branch tmp cool-feature

    # Rebase cool-feature onto trunk
    $ git rebase --onto upstream/master upstream/master cool-feature

In this situation, where you are already on branch ``cool-feature``, the last
command can be written more succinctly as:

.. code-block:: bash

    $ git rebase upstream/master

When all looks good you can delete your backup branch:

.. code-block:: bash

   $ git branch -D tmp

If it doesn't look good you may need to have a look at
:ref:`recovering-from-mess-up`.

If you have made changes to files that have also changed in trunk, this may
generate merge conflicts that you need to resolve - see the `git rebase`_ man
page for some instructions at the end of the "Description" section. There is
some related help on merging in the git user manual - see `resolving a
merge`_.

If your feature branch is already on GitHub and you rebase, you will have to force
push the branch; a normal push would give an error. If the branch you rebased is
called ``cool-feature`` and your GitHub fork is available as the remote called ``origin``,
you use this command to force-push:

.. code-block:: bash

   $ git push -f origin cool-feature

Note that this will overwrite the branch on GitHub, i.e. this is one of the few ways
you can actually lose commits with git.
Also note that it is never allowed to force push to the main mne-python repo (typically
called ``upstream``), because this would re-write commit history and thus cause problems
for all others.

.. _recovering-from-mess-up:

Recovering from mess-ups
^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes, you mess up merges or rebases. Luckily, in git it is relatively
straightforward to recover from such mistakes.

If you mess up during a rebase:

.. code-block:: bash

   $ git rebase --abort

If you notice you messed up after the rebase:

.. code-block:: bash

   # Reset branch back to the saved point
   $ git reset --hard tmp

If you forgot to make a backup branch:

.. code-block:: bash

   # Look at the reflog of the branch
   $ git reflog show cool-feature

   8630830 cool-feature@{0}: commit: BUG: io: close file handles immediately
   278dd2a cool-feature@{1}: rebase finished: refs/heads/my-feature-branch onto 11ee694744f2552d
   26aa21a cool-feature@{2}: commit: BUG: lib: make seek_gzip_factory not leak gzip obj
   ...

   # Reset the branch to where it was before the botched rebase
   $ git reset --hard cool-feature@{2}

Otherwise, googling the issue may be helpful (especially links to Stack
Overflow).

.. _rewriting-commit-history:

Rewriting commit history
^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   Do this only for your own feature branches.

There's an embarrassing typo in a commit you made? Or perhaps the you
made several false starts you would like the posterity not to see.

This can be done via *interactive rebasing*.

Suppose that the commit history looks like this:

.. code-block:: bash

    $ git log --oneline
    eadc391 Fix some remaining bugs
    a815645 Modify it so that it works
    2dec1ac Fix a few bugs + disable
    13d7934 First implementation
    6ad92e5 * masked is now an instance of a new object, MaskedConstant
    29001ed Add pre-nep for a copule of structured_array_extensions.
    ...

and ``6ad92e5`` is the last commit in the ``cool-feature`` branch. Suppose we
want to make the following changes:

* Rewrite the commit message for ``13d7934`` to something more sensible.
* Combine the commits ``2dec1ac``, ``a815645``, ``eadc391`` into a single one.

We do as follows:

.. code-block:: bash

    # make a backup of the current state
    $ git branch tmp HEAD
    # interactive rebase
    $ git rebase -i 6ad92e5

This will open an editor with the following text in it::

    pick 13d7934 First implementation
    pick 2dec1ac Fix a few bugs + disable
    pick a815645 Modify it so that it works
    pick eadc391 Fix some remaining bugs

    # Rebase 6ad92e5..eadc391 onto 6ad92e5
    #
    # Commands:
    #  p, pick = use commit
    #  r, reword = use commit, but edit the commit message
    #  e, edit = use commit, but stop for amending
    #  s, squash = use commit, but meld into previous commit
    #  f, fixup = like "squash", but discard this commit's log message
    #
    # If you remove a line here THAT COMMIT WILL BE LOST.
    # However, if you remove everything, the rebase will be aborted.
    #

To achieve what we want, we will make the following changes to it::

    r 13d7934 First implementation
    pick 2dec1ac Fix a few bugs + disable
    f a815645 Modify it so that it works
    f eadc391 Fix some remaining bugs

This means that (i) we want to edit the commit message for ``13d7934``, and
(ii) collapse the last three commits into one. Now we save and quit the
editor.

Git will then immediately bring up an editor for editing the commit message.
After revising it, we get the output::

    [detached HEAD 721fc64] FOO: First implementation
     2 files changed, 199 insertions(+), 66 deletions(-)
    [detached HEAD 0f22701] Fix a few bugs + disable
     1 files changed, 79 insertions(+), 61 deletions(-)
    Successfully rebased and updated refs/heads/my-feature-branch.

and the history looks now like this::

     0f22701 Fix a few bugs + disable
     721fc64 ENH: Sophisticated feature
     6ad92e5 * masked is now an instance of a new object, MaskedConstant

If it went wrong, recovery is again possible as explained :ref:`above
<recovering-from-mess-up>`.

Fetching a pull request
^^^^^^^^^^^^^^^^^^^^^^^

To fetch a pull request on the main repository to your local working
directory as a new branch, just do:

.. code-block:: bash

   $ git fetch upstream pull/<pull request number>/head:<local-branch>

As an example, to pull the realtime pull request which has a url
``https://github.com/mne-tools/mne-python/pull/615/``, do:

.. code-block:: bash

   $ git fetch upstream pull/615/head:realtime

If you want to fetch a pull request to your own fork, replace
``upstream`` with ``origin``. That's it!

Skipping a build
^^^^^^^^^^^^^^^^

The builds when the pull request is in `WIP` state can be safely skipped. The important thing is to ensure that the builds pass when the PR is ready to be merged. To skip a Travis build, add ``[ci skip]`` to the commit message::

  FIX: some changes [ci skip]

This will help prevent clogging up Travis and Appveyor and also save the environment.
