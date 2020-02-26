..  Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


       Chapter 0

       Preface

       ˆ Studying complexity science provides an opportunity to learn about di-

       | verse physical and social systems, to develop and apply programming
       | skills, and to think about fundamental questions in the philosophy of
       | science.

       | By reading this book and working on the exercises you will have a chance to
       | explore topics and ideas you might not encounter otherwise, practice program-
       | ming in Python, and learn more about data structures and algorithms.

       Features of this book include:

       Technical details Most books about complexity science are written for a

       | popular audience. They leave out technical details, which is frustrating
       | for people who can handle them. This book presents the code, the math,
       | and the explanations you need to understand how the models work.

       Further reading Throughout the book, I include pointers to further reading,

       | including original papers (most of which are available electronically) and
       | related articles from Wikipedia and other sources.

       Jupyter notebooks For each chapter I provide a Jupyter notebook that in-

       | cludes the code from the chapter, additional examples, and animations
       | that let you see the models in action.

       Exercises and solutions At the end of each chapter I suggest exercises you

       might want to work on, with solutions.

       | For most of the links in this book I use URL redirection. This mechanism has
       | the drawback of hiding the link destination, but it makes the URLs shorter
       | and less obtrusive. Also, and more importantly, it allows me to update the
       | links without updating the book. If you find a broken link, please let me know
       | and I will change the redirection.

       0.1

       Who is this book for?

       | The examples and supporting code for this book are in Python. You should
       | know core Python and be familiar with its object-oriented features, specifically
       | using and defining classes.

    .. container::
       :name: page14-div

       |background image|
       0.2

       Changes from the first edition

       xiii

       | If you are not already familiar with Python, you might want to start with
       | Think Python, which is appropriate for people who have never programmed
       | before. If you have programming experience in another language, there are
       | many good Python books to choose from, as well as online resources.

       | I use NumPy, SciPy, and NetworkX throughout the book. If you are familiar
       | with these libraries already, that’s great, but I will also explain them when
       | they appear.

       | I assume that the reader knows some mathematics: I use logarithms in several
       | places, and vectors in one example. But that’s about it.

       0.2

       Changes from the first edition

       | For the second edition, I added two chapters, one on evolution, the other on
       | the evolution of cooperation.

       | In the first edition, each chapter presented background on a topic and sug-
       | gested experiments the reader could run. For the second edition, I have done
       | those experiments. Each chapter presents the implementation and results as
       | a worked example, then suggests additional experiments for the reader.

       | For the second edition, I replaced some of my own code with standard libraries
       | like NumPy and NetworkX. The result is more concise and more efficient, and
       | it gives readers a chance to learn these libraries.

       | Also, the Jupyter notebooks are new. For every chapter there are two note-
       | books: one contains the code from the chapter, explanatory text, and exercises;
       | the other contains solutions to the exercises.

       | Finally, all supporting software has been updated to Python 3 (but most of it
       | runs unmodified in Python 2).

       0.3

       Using the code

       All code used in this book is available from a Git repository on GitHub:

       `http: <http://thinkcomplex.com/repo>`__

       `//thinkcomplex.com/repo <http://thinkcomplex.com/repo>`__

       `.  <http://thinkcomplex.com/repo>`__\ If you are not familiar with Git, it is a version

    .. container::
       :name: page15-div

       |background image|
       xiv

       Chapter 0

       Preface

       | control system that allows you to keep track of the files that make up a project.
       | A collection of files under Git’s control is called a “repository”. GitHub is a
       | hosting service that provides storage for Git repositories and a convenient web
       | interface.

       | The GitHub homepage for my repository provides several ways to work with
       | the code:

       ˆ You can create a copy of my repository by pressing the Fork button in

       | the upper right. If you don’t already have a GitHub account, you’ll need
       | to create one. After forking, you’ll have your own repository on GitHub
       | that you can use to keep track of code you write while working on this
       | book. Then you can clone the repo, which means that you copy the files
       | to your computer.

       ˆ Or you can clone my repository without forking; that is, you can make

       | a copy of my repo on your computer. You don’t need a GitHub account
       | to do this, but you won’t be able to write your changes back to GitHub.

       ˆ If you don’t want to use Git at all, you can download the files in a Zip

       file using the green button that says “Clone or download”.

       | I developed this book using Anaconda from Continuum Analytics, which is a
       | free Python distribution that includes all the packages you’ll need to run the
       | code (and lots more). I found Anaconda easy to install. By default it does
       | a user-level installation, not system-level, so you don’t need administrative
       | privileges. And it supports both Python 2 and Python 3. You can download
       | Anaconda from

       https://continuum.io/downloads

       `. <https://continuum.io/downloads>`__

       | The repository includes both Python scripts and Jupyter notebooks. If you
       | have not used Jupyter before, you can read about it at

       https://jupyter.org

       `. <https://jupyter.org>`__

       There are three ways you can work with the Jupyter notebooks:

       Run Jupyter on your computer If you installed Anaconda, you can in-

       | stall Jupyter by running the following command in a terminal or Com-
       | mand Window:

       $ conda install jupyter

    .. container::
       :name: page16-div

       |background image|
       0.3

       Using the code

       xv

       | Before you launch Jupyter, you should cd into the directory that contains
       | the code:

       $ cd ThinkComplexity2/code

       And then start the Jupyter server:

       $ jupyter notebook

       | When you start the server, it should launch your default web browser or
       | create a new tab in an open browser window. Then you can open and
       | run the notebooks.

       Run Jupyter on Binder Binder is a service that runs Jupyter in a virtual

       machine. If you follow this link,

       http://thinkcomplex.com/binder

       `, <http://thinkcomplex.com/binder>`__

       | you should get a Jupyter home page with the notebooks for this book
       | and the supporting data and scripts.

       | You can run the scripts and modify them to run your own code, but the
       | virtual machine you run them in is temporary. If you leave it idle, the
       | virtual machine disappears along with any changes you made.

       View notebooks on GitHub GitHub provides a view of the notebooks you

       | can can use to read the notebooks and see the results I generated, but
       | you won’t be able to modify or run the code.

       Good luck, and have fun!

       | Allen B. Downey
       | Professor of Computer Science
       | Olin College of Engineering
       | Needham, MA

       Contributor List

       | If you have a suggestion or correction, please send email to downey@allendowney.com.
       | If I make a change based on your feedback, I will add you to the contributor
       | list (unless you ask to be omitted).

       | Let me know what version of the book you are working with, and what format.
       | If you include at least part of the sentence the error appears in, that makes it
       | easy for me to search. Page and section numbers are fine, too, but not quite
       | as easy to work with. Thanks!

    .. container::
       :name: page17-div

       |background image|
       xvi

       Chapter 0

       Preface

       ˆ John Harley, Jeff Stanton, Colden Rouleau and Keerthik Omanakuttan are

       Computational Modeling students who pointed out typos.

       ˆ Jose Oscar Mur-Miranda found several typos.

       ˆ Phillip Loh, Corey Dolphin, Noam Rubin and Julian Ceipek found typos and

       made helpful suggestions.

       ˆ Sebastian Sch¨oner sent two pages of corrections!

       ˆ Philipp Marek sent a number of corrections.

       ˆ Jason Woodard co-taught Complexity Science with me at Olin College, intro-

       duced me to NK models, and made many helpful suggestions and corrections.

       ˆ Davi Post sent several corrections and suggestions.

       ˆ Graham Taylor sent a pull request on GitHub that fixed many typos.

       | I would especially like to thank the technical reviewers, Vincent Knight and Eric
       | Ma, who made many helpful suggestions, and the copy editor, Charles Roumeliotis,
       | who caught many errors and inconsistencies.

       | Other people who reported errors include Richard Hollands, Muhammad Najmi bin
       | Ahmad Zabidi, Alex Hantman, and Jonathan Harford.
