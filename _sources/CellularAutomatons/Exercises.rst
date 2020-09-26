..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Exercises
---------

The code for this chapter is in the Jupyter notebook chap07.ipynb_ in the repository for this book. Open this notebook, read the code, and run the cells. You can use this notebook to work on the exercises in this chapter.

**Exercise 1:**  Write a version of ``correlate`` that returns the same result as ``np.correlate`` with ``mode='same'``. Hint: use the NumPy function pad.

**Exercise 2:**  This exercise asks you to experiment with Rule 110 and some of its spaceships.

1. Read the Wikipedia page about Rule 110, which describes its background pattern and spaceships.
2. Create a Rule 110 CA with an initial condition that yields the stable background pattern. Note that the ``Cell1D`` class provides ``start_string``, which allows you to initialize the state of the array using a string of 1s and 0s.
3. Modify the initial condition by adding different patterns in the center of the row and see which ones yield spaceships. You might want to enumerate all possible patterns of n bits, for some reasonable value of n. For each spaceship, can you find the period and rate of translation? What is the biggest spaceship you can find?
4. What happens when spaceships collide?

**Exercise 3:**  The goal of this exercise is to implement a Turing machine.

1. Read about Turing machines.
2. Write a class called ``Turing`` that implements a Turing machine. For the action table, use the rules for a 3-state busy beaver.
3. Write a class named ``TuringViewer`` that generates an image that represents the state of the tape and the position and state of the head. For one example of what that might look like.

.. _chap07.ipynb: https://colab.research.google.com/github/pearcej/complex-colab/blob/master/notebooks/chap07.ipynb
