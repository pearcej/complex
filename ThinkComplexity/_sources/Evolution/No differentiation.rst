No differentiation
-------------------

Before we run the simulation, we have to specify the behavior of choose_dead and choose_replacements. We’ll start with simple versions of these functions that don’t depend on fitness:

::

    # class Simulation

        def choose_dead(self, fits):
            n = len(self.agents)
            is_dead = np.random.random(n) < 0.1
            index_dead = np.nonzero(is_dead)[0]
            return index_dead

In choose_dead, n is the number of agents and is_dead is a boolean array that contains True for the agents who die during this time step. In this version, every agent has the same probability of dying: 0.1. choose_dead uses np.nonzero to find the indices of the non-zero elements of is_dead (True is considered non-zero).

::

    # class Simulation

        def choose_replacements(self, n, fits):
            agents = np.random.choice(self.agents, size=n, replace=True)
            replacements = [agent.copy() for agent in agents]
            return replacements

In choose_replacements, n is the number of agents who reproduce during this time step. It uses np.random.choice to choose n agents with replacement. Then it invokes copy on each one and returns a list of new Agent objects.

These methods don’t depend on fitness, so this simulation does not have differential survival or reproduction. As a result, we should not expect to see evolution. But how can we tell?


