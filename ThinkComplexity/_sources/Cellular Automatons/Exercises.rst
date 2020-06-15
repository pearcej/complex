Exercises
---------

The code for this chapter is in the Jupyter notebook ``chap05.ipynb`` in the repository for this book. Open this notebook, read the code, and run the cells. You can use this notebook to work on the exercises in this chapter. My solutions are in ``chap05soln.ipynb``.

**Exercise 1:**  Write a version of ``correlate`` that returns the same result as ``np.correlate`` with ``mode='same'``. Hint: use the NumPy function pad.

**Exercise 2:**  This exercise asks you to experiment with Rule 110 and some of its spaceships.

1. Read the Wikipedia page about Rule 110, which describes its background pattern and spaceships: http://thinkcomplex.com/r110.
2. Create a Rule 110 CA with an initial condition that yields the stable background pattern. Note that the ``Cell1D`` class provides ``start_string``, which allows you to initialize the state of the array using a string of 1s and 0s.
3. Modify the initial condition by adding different patterns in the center of the row and see which ones yield spaceships. You might want to enumerate all possible patterns of n bits, for some reasonable value of n. For each spaceship, can you find the period and rate of translation? What is the biggest spaceship you can find?
4. What happens when spaceships collide?

**Exercise 3:**  The goal of this exercise is to implement a Turing machine.

1. Read about Turing machines at http://thinkcomplex.com/tm.
2. Write a class called ``Turing`` that implements a Turing machine. For the action table, use the rules for a 3-state busy beaver.
3. Write a class named ``TuringViewer`` that generates an image that represents the state of the tape and the position and state of the head. For one example of what that might look like, see http://thinkcomplex.com/turing.

**Exercise 4:**  This exercise asks you to implement and test several PRNGs. For testing, you will need to install ``DieHarder``, which you can download from http://thinkcomplex.com/dh, or it might be available as a package for your operating system.

1. Write a program that implements one of the linear congruential generators described at http://thinkcomplex.com/lcg. Test it using ``DieHarder``.
2. Read the documentation of Python’s ``random`` module. What PRNG does it use? Test it.
3. Implement a Rule 30 CA with a few hundred cells, run it for as many time steps as you can in a reasonable amount of time, and output the center column as a sequence of bits. Test it.

**Exercise 5:**  Falsifiability is an appealing and useful idea, but among philosophers of science it is not generally accepted as a solution to the demarcation problem, as Popper claimed.

Read http://thinkcomplex.com/false and answer the following questions.

1. What is the demarcation problem?
2. How, according to Popper, does falsifiability solve the demarcation problem?
3. Give an example of two theories, one considered scientific and one considered unscientific, that are successfully distinguished by the criterion of falsifiability.
4. Can you summarize one or more of the objections that philosophers and historians of science have raised to Popper’s claim?
5. Do you get the sense that practicing philosophers think highly of Popper’s work?