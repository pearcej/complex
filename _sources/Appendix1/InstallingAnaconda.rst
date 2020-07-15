.. _Ap_1:

Installing Juypter Notebooks through Anaconda
---------------------------------------------

If you don't already have Jupyter, I highly recommend installing Anaconda, which is a Python distribution that contains everything you need for the workshop. It is easy to install on Windows, Mac, and Linux, and because it does a user-level install, it will not interfere with other Python installations.

Information about installing Anaconda is here: https://www.anaconda.com/products/individual

The code for the tutorial works in Python 2 and Python 3, but I recommend Python 3.

When you install Anaconda, you should get Jupyter by default, but if not, run

:: 

    conda install jupyter

Once you have Jupyter, you can get my code from this Git repository on Github. If you have a Git client installed, you should be able to download it by running:

::

    git clone https://github.com/AllenDowney/ThinkComplexity2.git

It should create a directory named ThinkComplexity2. Otherwise you can download the repository in this zip file and unzip it.

Then cd into the new directory:

::

    cd ThinkComplexity2

To make sure you have the packages you need, you can use environment.yml to create a Conda environment named complexity

::

   conda env create -f environment.yml

Then activate the new environment

::

  conda activate complexity

To start Jupyter, run:

::

    cd code
    jupyter notebook

Jupyter should launch your default browser or open a tab in an existing browser window. If not, the Jupyter server should print a URL you can use. For example, when I launch Jupyter, I get

::

    ~/ThinkComplexity2$ jupyter notebook
    [I 10:03:20.115 NotebookApp] Serving notebooks from local directory: /home/downey/ThinkComplexity2
    [I 10:03:20.115 NotebookApp] 0 active kernels
    [I 10:03:20.115 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 10:03:20.115 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

In this case, the URL is http://localhost:8888.
When you start your server, you might get a different URL. Whatever it is, if you paste it into a browser, you should should see a home page with a list of the notebooks in the repository.

Click on chap09.ipynb. It should open the notebook for Chapter 9.

Select the cell with the import statements and press "Shift-Enter" to run the code in the cell. If it works and you get no error messages, you are all set.

If you get error messages about missing packages, you can install the packages you need using your package manager, or install Anaconda.

If you have trouble with the animations, you might have to install ffmpeg. The animations are not necessary for the tutorial.    