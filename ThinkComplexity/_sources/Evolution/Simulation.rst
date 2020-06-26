Simulation
---------------

.. _12.5:

Now that we have agents and a fitness landscape, I’ll define a class called ``Simulation`` that simulates the creation, reproduction, and death of the agents. To avoid getting bogged down, I’ll present a simplified version of the code here; you can see the details in the notebook for this chapter.

Here’s the definition of ``Simulation``:

::

    class Simulation:

        def __init__(self, fit_land, agents):
            self.fit_land = fit_land
            self.agents = agents

The attributes of a Simulation are:

- ``fit_land``: A reference to a FitnessLandscape object.
- ``agents``: An array of Agent objects.

The most important function in Simulation is step, which simulates one time step:

::

    # class Simulation:

        def step(self):
            n = len(self.agents)
            fits = self.get_fitnesses()

            # see who dies
            index_dead = self.choose_dead(fits)
            num_dead = len(index_dead)

            # replace the dead with copies of the living
            replacements = self.choose_replacements(num_dead, fits)
            self.agents[index_dead] = replacements

step uses three other methods:

- ``get_fitnesses`` returns an array containing the fitness of each agent.
- ``choose_dead`` decides which agents die during this time step, and returns an array that contains the indices of the dead agents.
- ``choose_replacements`` decides which agents reproduce during this time step, invokes copy on each one, and returns an array of new ``Agent`` objects.

In this version of the simulation, the number of new agents during each time step equals the number of dead agents, so the number of live agents is constant.

.. mchoice:: q_12.5
   :answer_a: If an agent dies then a new agent will be made in the next time step so the amount of agents is always changing.
   :answer_b: If an agent dies no new agent will take its place leading to all the agents being dead eventually. 
   :answer_c: If an agent dies then a new agent is made within that same time step so that the number of live agents is constant.  
   :answer_d: None of the above.
   :correct: c
   :feedback_a: Sorry but when one agent dies another is made within that same time step so the amount of agents is constant.  
   :feedback_b: Sorry but a new agent will be made to replace an agent if it dies. 
   :feedback_c: Correct!
   :feedback_d: Incorrect. There is one correct answer.

   What happens when an agent dies in this version of the simulation? 




