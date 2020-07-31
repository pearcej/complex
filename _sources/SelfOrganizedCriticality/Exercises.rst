Exercises
---------
The code for this chapter is in the Jupyter notebook chap10.ipynb_ in the repository for this book. Open this notebook, read the code, and run the cells. You can use this notebook to work on the following exercises. 

**Exercise 1:** To test whether the distributions of ``T`` and ``S`` are heavy-tailed, we plotted their PMFs on a log-log scale, which is what Bak, Tang and Wiesenfeld show in their paper. But as we saw in :ref:`Section 6.8 <SFN_8>`, this visualization can obscure the shape of the distribution. Using the same data, make a plot that shows the cumulative distributions (CDFs) of ``S`` and ``T``. What can you say about their shape? Do they follow a power law? Are they heavy-tailed?

You might find it helpful to plot the CDFs on a log-x scale and on a log-log scale.

**Exercise 2:** In :ref:`Section 10.6<SOC_6>` we showed that the initial configuration of the sand pile model produces fractal patterns. But after we drop a large number of random grains, the patterns look more random.

Starting with the example in :ref:`Section 10.6<SOC_6>`, run the sand pile model for a while and then compute fractal dimensions for each of the 4 levels. Is the sand pile model fractal in steady state?

**Exercise 3:** Another version of the sand pile model, called the “single source” model, starts from a different initial condition: instead of all cells at the same level, all cells are set to 0 except the center cell, which is set to a large value. Write a function that creates a SandPile object, sets up the single source initial condition, and runs until the pile reaches equilibrium. Does the result appear to be fractal?



**Exercise 4:** In their 1989 paper, Bak, Chen and Creutz suggest that the Game of Life is a self-organized critical system.

To replicate their tests, start with a random configuration and run the GoL CA until it stabilizes. Then choose a random cell and flip it. Run the CA until it stabilizes again, keeping track of ``T``, the number of time steps it takes, and ``S``, the number of cells affected. Repeat for a large number of trials and plot the distributions of ``T`` and ``S``. Also, estimate the power spectrums of ``T`` and ``S`` as signals in time, and see if they are consistent with pink noise.

**Exercise 5:** In The Fractal Geometry of Nature, Benoit Mandelbrot proposes what he calls a “heretical” explanation for the prevalence of heavy-tailed distributions in natural systems. It may not be, as Bak suggests, that many systems can generate this behavior in isolation. Instead there may be only a few, but interactions between systems might cause the behavior to propagate.

To support this argument, Mandelbrot points out:

- The distribution of observed data is often “the joint effect of a fixed underlying true distribution and a highly variable filter”.
- Heavy-tailed distributions are robust to filtering; that is, “a wide variety of filters leave their asymptotic behavior unchanged”.

What do you think of this argument? Would you characterize it as reductionist or holist?

**Exercise 6:** Read about the “Great Man” theory of history. What implication does self-organized criticality have for this theory?

.. _chap10.ipynb: https://colab.research.google.com/github/pearcej/complex-colab/blob/master/notebooks/chap10.ipynb