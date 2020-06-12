Exercises
----------

The code for this chapter is in the Jupyter notebook chap11.ipynb in the repository for this book. Open the notebook, read the code, and run the cells. You can use the notebook to work on the following exercises. My solutions are in chap11soln.ipynb.

**Exercise 1:**  The notebook shows the effects of differential reproductions and survival separately. What if you have both? Write a class called SimWithBoth that uses the version of choose_dead from SimWithDiffSurvival and the version of choose_replacements from SimWithDiffReproduction. Does mean fitness increase more quickly?

As a Python challenge, can you write this class without copying code?

**Exercise 2:**  When we change the landscape as in Section ??, the number of occupied locations and the mean distance usually increase, but the effect is not always big enough to be obvious. Try out some different random seeds to see how general the effect is.

1
    This model is a variant of the NK model developed primarily by Stuart Kauffman (see http://thinkcomplex.com/nk).

    