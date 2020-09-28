
Sugarscape
-----------

.. _ABM_5:

.. _ABM_FIG_3:

In 1996 Joshua Epstein and Robert Axtell proposed Sugarscape, an agent-based model of an “artificial society” intended to support experiments related to economics and other social sciences.

Sugarscape is a versatile model that has been adapted for a wide variety of topics. As examples, we will replicate the first few experiments from Epstein and Axtell’s book, *Growing Artificial Societies*.

In its simplest form, Sugarscape is a model of a simple economy where agents move around on a 2-D grid, harvesting and accumulating “sugar”, which represents economic wealth. Some parts of the grid produce more sugar than others, and some agents are better at finding it than others.

This version of Sugarscape is often used to explore and explain the distribution of wealth, in particular the tendency toward inequality.

In the Sugarscape grid, each cell has a capacity, which is the maximum amount of sugar it can hold. In the original configuration, there are two high-sugar regions, with capacity 4, surrounded by concentric rings with capacities 3, 2, and 1.


.. figure:: Figures/SUG_MODEL.png
    :align: center
    :alt: "Figure 11.3: Replication of the original Sugarscape model: initial configuration (left), after 2 steps (middle) and after 100 steps (right)."

    Figure 11.3: Replication of the original Sugarscape model: initial configuration (left), after 2 steps (middle) and after 100 steps (right).

:ref:`Figure 11.3 <ABM_FIG_3>` (left) shows the initial configuration, with the darker areas indicating cells with higher capacity, and small dots representing the agents.

Initially there are 400 agents placed at random locations. Each agent has three randomly-chosen attributes:

**Sugar:**  Each agent starts with an endowment of sugar chosen from a uniform distribution between 5 and 25 units.

**Metabolism:**  Each agent has some amount of sugar they must consume per time step, chosen uniformly between 1 and 4.

**Vision:**  Each agent can “see” the amount of sugar in nearby cells and move to the cell with the most, but some agents can see and move farther than others. The distance agents see is chosen uniformly between 1 and 6.

During each time step, agents move one at a time in a random order. Each agent follows these rules:

- The agent surveys ``k`` cells in each of the 4 compass directions, where ``k`` is the range of the agent’s vision.
- It chooses the unoccupied cell with the most sugar. In case of a tie, it chooses the closer cell; among cells at the same distance, it chooses randomly.
- The agent moves to the selected cell and harvests the sugar, adding the harvest to its accumulated wealth and leaving the cell empty.
- The agent consumes some part of its wealth, depending on its metabolism. If the resulting total is negative, the agent “starves” and is removed.

After all agents have executed these steps, the cells grow back some sugar, typically 1 unit, but the total sugar in each cell is bounded by its capacity.

:ref:`Figure 11.3 <ABM_FIG_3>` (middle) shows the state of the model after two steps. Most agents are moving toward the areas with the most sugar. Agents with high vision move the fastest; agents with low vision tend to get stuck on the plateaus, wandering randomly until they get close enough to see the next level.

Agents born in the areas with the least sugar are likely to starve unless they have a high initial endowment and high vision.

Within the high-sugar areas, agents compete with each other to find and harvest sugar as it grows back. Agents with high metabolism or low vision are the most likely to starve.

When sugar grows back at 1 unit per time step, there is not enough sugar to sustain the 400 agents we started with. The population drops quickly at first, then more slowly, and levels off around 250.

:ref:`Figure 11.3 <ABM_FIG_3>` (right) shows the state of the model after 100 time steps, with about 250 agents. The agents who survive tend to be the lucky ones, born with high vision and/or low metabolism. Having survived to this point, they are likely to survive forever, accumulating unbounded stockpiles of sugar.

.. figure:: Figures/Initial_Sugarscape.gif
    :align: center
    :alt: "Gif 11.1: Initial Sugarscape for 100 steps."

    Gif 11.1: Initial Sugarscape for 100 steps.

.. mchoice:: q_10.4
   :answer_a: They are a model of a simple economy.
   :answer_b: Agents move around a 3-D grid.
   :answer_c: They are often used to explore and explain the distribution of wealth.
   :answer_d: All of the agents in the sugarscape are able to hold the same amount of sugar and are all just as likely to locate sugar.
   :answer_e: None of the above are related to sugarscapes.
   :correct: a,c
   :feedback_a: Correct!
   :feedback_b: Sorry they do use grids but they use 2-D grids.
   :feedback_c: Correct!
   :feedback_d: Sorry but some agents are better than others at finding sugar.
   :feedback_e: Sorry two of the answers given above are correct.

   Which of the following are true about Sugarscapes:
