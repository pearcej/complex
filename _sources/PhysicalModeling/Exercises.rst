..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Exercises
---------

**Exercise 1:** In :ref:`Section 9.7<PM_7>` we showed that the Rule 18 CA produces a fractal. Can you find other 1-D CAs that produce fractals?

Note: the ``Cell1D`` object does not wrap around from the left edge to the right, which creates artifacts at the boundaries for some rules. You might want to use ``Wrap1D``, which is a child class of ``Cell1D`` that wraps around. It is defined in ``Cell1D.py`` in the repository for this book.

**Exercise 2:** In 1990 Bak, Chen and Tang proposed a cellular automaton that is an abstract model of a forest fire. Each cell is in one of three states: empty, occupied by a tree, or on fire.

The rules of the CA are:

1. An empty cell becomes occupied with probability p.

2. A cell with a tree burns if any of its neighbors is on fire.

3. A cell with a tree spontaneously burns, with probability f, even if none of its neighbors is on fire.

4. A cell with a burning tree becomes an empty cell in the next time step.

Write a program that implements this model. You might want to inherit from ``Cell2D``. Typical values for the parameters are ``p=0.01`` and ``f=0.001``, but you might want to experiment with other values.

Starting from a random initial condition, run the model until it reaches a steady state where the number of trees no longer increases or decreases consistently.

In steady state, is the geometry of the forest fractal? What is its fractal dimension?
