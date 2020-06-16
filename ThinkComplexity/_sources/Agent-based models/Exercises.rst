Exercises
----------

The code for this chapter is in the Jupyter notebook ``chap09.ipynb`` in the repository for this book. Open this notebook, read the code, and run the cells. You can use this notebook to work on the following exercises. My solutions are in ``chap09soln.ipynb``.


**Exercise 1:**  Bill Bishop, author of *The Big Sort*, argues that American society is increasingly segregated by political opinion, as people choose to live among like-minded neighbors.

The mechanism Bishop hypothesizes is not that people, like the agents in Schelling’s model, are more likely to move if they are isolated, but that when they move for any reason, they are likely to choose a neighborhood with people like themselves.

Modify your implementation of Schelling’s model to simulate this kind of behavior and see if it yields similar degrees of segregation.

There are several ways you can model Bishop’s hypothesis. In my implementation, a random selection of agents moves during each step. Each agent considers k randomly-chosen empty locations and chooses the one with the highest fraction of similar neighbors. How does the degree of segregation depend on k?

**Exercise 2:**  In the first version of SugarScape, we never add agents, so once the population falls, it never recovers. In the second version, we only replace agents when they die, so the population is constant. Now let’s see what happens if we add some “population pressure”.

Write a version of SugarScape that adds a new agent at the end of every step. Add code to compute the average vision and the average metabolism of the agents at the end of each step. Run the model for a few hundred steps and plot the population over time, as well as the average vision and average metabolism.

You should be able to implement this model by inheriting from ``SugarScape`` and overriding ``__init__`` and ``step``.

**Exercise 3:**  Among people who study philosophy of mind, “Strong AI" is the theory that an appropriately-programmed computer could have a mind in the same sense that humans have minds.



John Searle presented a thought experiment called “The Chinese Room”, intended to show that Strong AI is false. You can read about it at http://thinkcomplex.com/searle.


What is the **system reply** to the Chinese Room argument? How does what you have learned about emergence influence your reaction to the system response?



