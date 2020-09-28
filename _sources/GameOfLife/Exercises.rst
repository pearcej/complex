..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Exercises
---------

The code for this chapter is in the notebook chap08.ipynb_ in the repository for this book. Open this notebook, read the code, and run the cells. You can use this notebook to work on the following exercises.

**Exercise 1:** Start GoL in a random state and run it until it stabilizes. What stable patterns can you identify?

**Exercise 2:** Many named patterns are available in portable file formats. Modify ``Life.py`` to parse one of these formats and initialize the grid.

**Exercise 3:** In the given implementation, the ``Life`` class is based on a parent class called ``Cell2D``, and the ``LifeViewer`` class is based on ``Cell2DViewer``. You can use these base classes to implement other 2-D cellular automatons.

For example, one variation of GoL, called “Highlife”, has the same rules as GoL, plus one additional rule: a dead cell with 6 neighbors comes to life.

Write a class named Highlife that inherits from ``Cell2D`` and implements this version of the rules. Also write a class named ``HighlifeViewer`` that inherits from ``Cell2DViewer`` and try different ways to visualize the results. As a simple example, use a different colormap.

One of the more interesting patterns in Highlife is the replicator. Use ``add_cells`` to initialize Highlife with a replicator and see what it does.

**Exercise 4:** If you generalize the Turing machine to two dimensions, or add a read-write head to a 2-D CA, the result is a cellular automaton called a Turmite. It is named after a termite because of the way the read-write head moves, but spelled wrong as an homage to Alan Turing.

The most famous Turmite is Langton’s Ant, discovered by Chris Langton in 1986.

The ant is a read-write head with four states, which you can think of as facing north, south, east or west. The cells have two states, black and white.

The rules are simple. During each time step, the ant checks the color of the cell it is on. If black, the ant turns to the right, changes the cell to white, and moves forward one space. If the cell is white, the ant turns left, changes the cell to black, and moves forward.

Given a simple world, a simple set of rules, and only one moving part, you might expect to see simple behavior — but you should know better by now. Starting with all white cells, Langton’s ant moves in a seemingly random pattern for more than 10,000 steps before it enters a cycle with a period of 104 steps. After each cycle, the ant is translated diagonally, so it leaves a trail called the “highway”.

Write an implementation of Langton’s Ant.

.. _chap08.ipynb: https://colab.research.google.com/github/pearcej/complex-colab/blob/master/notebooks/chap08.ipynb
