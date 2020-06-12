..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
    To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Using the code
----------------

All code used in this book is available from a Git repository on GitHub: http://thinkcomplex.com/repo. If you are not familiar with Git, it is a version control system that allows you to keep track of the files that make up a project.
A collection of files under Git’s control is called a “repository”. GitHub is a hosting service that provides storage for Git repositories and a convenient web interface.

The GitHub homepage for my repository provides several ways to work with the code:

-  You can create a copy of my repository by pressing the Fork button in the upper right. If you don’t already have a GitHub account, you’ll need to create one. After forking, you’ll have your own repository on GitHub that you can use to keep track of code you write while working on this book. Then you can clone the repo, which means that you copy the files to your computer.

-  Or you can clone my repository without forking; that is, you can make a copy of my repo on your computer. You don’t need a GitHub account to do this, but you won’t be able to write your changes back to GitHub.

-  If you don’t want to use Git at all, you can download the files in a Zip file using the green button that says “Clone or download”.

I developed this book using Anaconda from Continuum Analytics, which is a free Python distribution that includes all the packages you’ll need to run the code (and lots more). I found Anaconda easy to install. By default it does a user-level installation, not system-level, so you don’t need administrative privileges. And it supports both Python 2 and Python 3. You can download Anaconda from https://continuum.io/downloads. The repository includes both Python scripts and Jupyter notebooks. If you have not used Jupyter before, you can read about it at https://jupyter.org. There are three ways you can work with the Jupyter notebooks:

The repository includes both Python scripts and Jupyter notebooks. If you have not used Jupyter before, you can read about it at https://jupyter.org.

There are three ways you can work with the Jupyter notebooks:

**Run Jupyter on your computer** If you installed Anaconda, you can install Jupyter by running the following command in a terminal or Command Window:

::

    $ conda install jupyter

Before you launch Jupyter, you should cd into the directory that contains the code:

::

    $ cd ThinkComplexity2/code

And then start the Jupyter server:

::

    $ jupyter notebook

When you start the server, it should launch your default web browser or create a new tab in an open browser window. Then you can open and run the notebooks.

**Run Jupyter on Binder**  Binder is a service that runs Jupyter in a virtual machine. If you follow this link, http://thinkcomplex.com/binder , you should get a Jupyter home page with the notebooks for this book and the supporting data and scripts.

You can run the scripts and modify them to run your own code, but the virtual machine you run them in is temporary. If you leave it idle, the virtual machine disappears along with any changes you made.

**View notebooks on GitHub**  GitHub provides a view of the notebooks you can can use to read the notebooks and see the results I generated, but you won’t be able to modify or run the code.

Good luck, and have fun!
Allen B. Downey
Professor of Computer Science
Olin College of Engineering
Needham, MA