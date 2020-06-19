Agents
-----------

Next we need agents. Here’s the class definition:

::

    class Agent:

        def __init__(self, loc, fit_land):
            self.loc = loc
            self.fit_land = fit_land
            self.fitness = fit_land.fitness(self.loc)

        def copy(self):
            return Agent(self.loc, self.fit_land)


The attributes of an Agent are:

- ``loc``: The location of the ``Agent`` in the fitness landscape.
- ``fit_land``: A reference to a ``FitnessLandscape`` object.
- ``fitness``: The fitness of this ``Agent`` in the ``FitnessLandscape``, represented as a number between 0 and 1.

``Agent`` provides ``copy``, which copies the genotype exactly. Later, we will see a version that copies with mutation, but mutation is not necessary for evolution.

