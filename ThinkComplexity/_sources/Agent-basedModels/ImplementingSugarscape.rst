Implementing Sugarscape
------------------------

Sugarscape is more complicated than the previous models, so I won’t present the entire implementation here. I will outline the structure of the code and you can see the details in the Jupyter notebook for this chapter, ``chap09.ipynb``, which is in the repository for this book. If you are not interested in the details, you can skip this section.

During each step, the agent moves, harvests sugar, and ages. Here is the ``Agent`` class and its ``step`` method:

::

    class Agent:

        def step(self, env):
            self.loc = env.look_and_move(self.loc, self.vision)
            self.sugar += env.harvest(self.loc) - self.metabolism
            self.age += 1

The parameter ``env`` is a reference to the environment, which is a ``Sugarscape`` object. It provides methods ``look_and_move`` and ``harvest``:

- ``look_and_move`` takes the location of the agent, which is a tuple of coordinates, and the range of the agent’s vision, which is an integer. It returns the agent’s new location, which is the visible cell with the most sugar.
- ``harvest`` takes the (new) location of the agent, and removes and returns the sugar at that location.

``Sugarscape`` inherits from ``Cell2D``, so it is similar to the other grid-based models we’ve seen.

The attributes include ``agents``, which is a list of ``Agent`` objects, and ``occupied``, which is a set of tuples, where each tuple contains the coordinates of a cell occupied by an agent.

Here is the ``Sugarscape`` class and its ``step`` method:

::

    class Sugarscape(Cell2D):

        def step(self):

            # loop through the agents in random order
            random_order = np.random.permutation(self.agents)
            for agent in random_order:

                # mark the current cell unoccupied
                self.occupied.remove(agent.loc)

                # execute one step
                agent.step(self)

                # if the agent is dead, remove from the list
                if agent.is_starving():
                    self.agents.remove(agent)
                else:
                    # otherwise mark its cell occupied
                    self.occupied.add(agent.loc)

            # grow back some sugar
            self.grow()
            return len(self.agents)

During each step, the Sugarscape uses the NumPy function ``permutation`` so it loops through the agents in random order. It invokes step on each agent and then checks whether it is dead. After all agents have moved, some of the sugar grows back. The return value is the number of agents still alive.

I won’t show more details here; you can see them in the notebook for this chapter. If you want to learn more about NumPy, you might want to look at these functions in particular:

- ``make_visible_locs``, which builds the array of locations an agent can see, depending on its vision. The locations are sorted by distance, with locations at the same distance appearing in random order. This function uses ``np.random.shuffle`` and ``np.vstack``.

- ``make_capacity``, which initializes the capacity of the cells using NumPy functions ``indices``, ``hypot``, ``minimum``, and ``digitize``.
- ``look_and_move``, which uses ``argmax``.



