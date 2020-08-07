Exercises
----------

The code for this chapter is in the Jupyter notebook chap13.ipynb_ in the repository for this book. Open the notebook, read the code, and run the cells. You can use the notebook to work on the following exercises. 

**Exercise 1:**  The notebook shows the effects of differential reproductions and survival separately. What if you have both? Write a class called ``SimWithBoth`` that uses the version of ``choose_dead`` from ``SimWithDiffSurvival`` and the version of ``choose_replacements`` from ``SimWithDiffReproduction``. Does mean fitness increase more quickly?

As a Python challenge, can you write this class without copying code?

**Exercise 2:**  When we change the landscape as in :ref:`Section 13.10 <EVO_10>`, the number of occupied locations and the mean distance usually increase, but the effect is not always big enough to be obvious. Try out some different random seeds to see how general the effect is.

.. _chap13.ipynb: https://colab.research.google.com/github/pearcej/complex-colab/blob/master/notebooks/chap13.ipynb