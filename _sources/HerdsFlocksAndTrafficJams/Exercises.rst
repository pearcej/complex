..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Exercises
---------

The code for the traffic jam simulation is in the Jupyter notebook chap12.ipynb_ in the repository for this book. Open this notebook, read the code, and run the cells. You can use this notebook to work on the following exercise.

**Exercise 1:**  In the traffic jam simulation, define a class, ``BetterDriver``, that inherits from ``Driver`` and ``overrides`` ``choose_acceleration``. See if you can define driving rules that do better than the basic implementation in ``Driver``. You might try to achieve higher average speed, or a lower number of collisions.

**Exercise 2:**  The code for the Boid implementation is in ``Boids7.py`` in the repository for this book. To run it, you will need VPython, a library for 3-D graphics and animation. If you use Anaconda, you can run the following in a terminal or Command Window:

::

    conda install -c vpython vpython

Then run ``Boids7.py``. It should either launch a browser or create a window in a running browser, and create an animated display showing Boids, as white cones, circling a red sphere, which is the carrot. If you click and move the mouse, you can move the carrot and see how the Boids react.

Read the code to see how the parameters control Boid behaviors. Experiment with different parameters. What happens if you “turn off” one of the behaviors by setting its weight to 0?


To generate more bird-like behavior, Flake suggests adding a behavior to maintain a clear line of sight; in other words, if there is another bird directly ahead, the Boid should move away laterally. What effect do you expect this rule to have on the behavior of the flock? Implement it and see.

**Exercise 3:** The view that free will is compatible with determinism is called compatibilism. One of the strongest challenges to compatibilism is the “consequence argument”. What is the consequence argument? What response can you give to the consequence argument based on what you have read in this book?

.. _chap12.ipynb: https://colab.research.google.com/github/pearcej/complex-colab/blob/master/notebooks/chap12.ipynb
