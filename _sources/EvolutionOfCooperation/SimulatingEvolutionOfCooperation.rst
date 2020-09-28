..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _EOC_5:

Simulating Evolution of Cooperation
-----------------------------------

*Evolution of Cooperation* is the title of the first book where Axelrod presented results from Prisoner’s Dilemma tournaments and discussed the implications for the problem of altruism. Since then, he and other researchers have explored the evolutionary dynamics of PD tournaments, that is, how the distribution of strategies changes over time in a population of PD contestants. In the rest of this chapter, we will run a version of those experiments and explore the results.

First, we’ll need a way to encode a PD strategy as a genotype. For this experiment, we consider strategies where the agent’s choice in each round depends only on the opponent’s choice in the previous two rounds. We represent a strategy using a dictionary that maps from the opponent’s previous two choices to the agent’s next choice.

Here is the class definition for these agents:

::

    class Agent:

        keys = [(None, None),
                (None, 'C'),
                (None, 'D'),
                ('C', 'C'),
                ('C', 'D'),
                ('D', 'C'),
                ('D', 'D')]

        def __init__(self, values, fitness=np.nan):
            self.values = values
            self.responses = dict(zip(self.keys, values))
            self.fitness = fitness

``keys`` is the sequence of keys in each agent’s dictionary, where the tuple ('C', 'C') means that the opponent cooperated in the previous two rounds; (None, 'C') means that only one round has been played and the opponent cooperated; and (None, None) means that no rounds have been played.

In the ``__init__`` method, ``values`` is a sequence of choices, either 'C' or 'D', that correspond to ``keys``. So if the first element of values is 'C', that means that this agent will cooperate in the first round. If the last element of ``values`` is 'D', this agent will defect if the opponent defected in the previous two rounds.

In this implementation, the genotype of an agent who always defects is 'DDDDDDD'; the genotype of an agent who always cooperates is 'CCCCCCC', and the genotype for TFT is 'CCDCDCD'.

The ``Agent`` class provides ``copy``, which makes another agent with the same genotype, but with some probability of mutation:

::

    def copy(self, prob_mutate=0.05):
        if np.random.random() > prob_mutate:
            values = self.values
        else:
            values = self.mutate()
        return Agent(values, self.fitness)

Mutation works by choosing a random value in the genotype and flipping from 'C' to 'D', or vice versa:

::

    def mutate(self):
        values = list(self.values)
        index = np.random.choice(len(values))
        values[index] = 'C' if values[index] == 'D' else 'D'
        return values

Now that we have agents, we need a tournament.

.. mchoice:: q_13.5.1
    :answer_a: CCCCCCC
    :answer_b: DDDDDDD
    :answer_c: CCDCDCD
    :answer_d: CDCDCDC
    :correct: d
    :feedback_a: Sorry, This if it all ways cooperates.
    :feedback_b: Sorry, this is always defect.
    :feedback_c: Sorry, this is TFT.
    :feedback_d: Correct!

    What would be the genotype for a strategy that always does the opposite of the round before?
