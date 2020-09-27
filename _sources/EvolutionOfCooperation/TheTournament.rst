..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _EOC_6:

The Tournament
--------------

The ``Tournament`` class encapsulates the details of the PD competition:

::

    payoffs = {('C', 'C'): (3, 3),
               ('C', 'D'): (0, 5),
               ('D', 'C'): (5, 0),
               ('D', 'D'): (1, 1)}

    num_rounds = 6

    def play(self, agent1, agent2):
        agent1.reset()
        agent2.reset()

        for i in range(self.num_rounds):
            resp1 = agent1.respond(agent2)
            resp2 = agent2.respond(agent1)

            pay1, pay2 = self.payoffs[resp1, resp2]

            agent1.append(resp1, pay1)
            agent2.append(resp2, pay2)

        return agent1.score, agent2.score

``payoffs`` is a dictionary that maps from the agents’ choices to their rewards. For example, if both agents cooperate, they each get 3 points. If one defects and the other cooperates, the defector gets 5 and the cooperator gets 0. If they both defect, each gets 1. These are the payoffs Axelrod used in his tournaments.

The ``play`` method runs several rounds of the PD game. It uses the following methods from the ``Agent`` class:

- ``reset``: Initializes the agents before the first round, resetting their scores and the history of their responses.
- ``respond``: Asks each agent for their response, given the opponent’s previous responses.
- ``append``: Updates each agent by storing the choices and adding up the scores from successive rounds.

After the given number of rounds, ``play`` returns the total score for each agent. I chose ``num_rounds=6`` so that each element of the genotype is accessed with roughly the same frequency. The first element is only accessed during the first round, or one sixth of the time. The next two elements are only accessed during the second round, or one twelfth each. The last four elements are accessed four of six times, or one sixth each, on average.

``Tournament`` provides a second method, ``melee``, that determines which agents compete against each other:

::

    def melee(self, agents, randomize=True):
        if randomize:
            agents = np.random.permutation(agents)

        n = len(agents)
        i_row = np.arange(n)
        j_row = (i_row + 1) % n

        totals = np.zeros(n)

        for i, j in zip(i_row, j_row):
            agent1, agent2 = agents[i], agents[j]
            score1, score2 = self.play(agent1, agent2)
            totals[i] += score1
            totals[j] += score2

        for i in i_row:
            agents[i].fitness = totals[i] / self.num_rounds / 2

``melee`` takes a list of agents and a boolean, ``randomize``, that determines whether each agent fights the same neighbors every time, or whether the pairings are randomized.

``i_row`` and ``j_row`` contain the indices of the pairings. totals contains the total score of each agent.

Inside the loop, we select two agents, invoke ``play``, and update ``totals``. At the end, we compute the average number of points each agent got, per round and per opponent, and store the results in the ``fitness`` attribute of each agent.

.. dragndrop:: Ch13.6_Q1
    :match_1: reset|||Initializes the agents before the first round, resetting their scores and the history of their responses.
    :match_2: respond|||Asks each agent for their response, given the opponent’s previous responses.
    :match_3: append|||Updates each agent by storing the choices and adding up the scores from successive rounds.
