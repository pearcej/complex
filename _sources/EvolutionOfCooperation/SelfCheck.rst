Self Check
----------------

.. fillintheblank:: SC13_Q1
    :casei:

    |blank| is the tendency of many animals to help other animals, even to their own detriment. This creates a conflict with |blank|, where it suggests that animals live in a state of constant competition.

    - :altruism: Correct!
      :x: Incorrect, please try again.
    
    - :natural selection: Correct!
      :x: Incorrect, please try again.

.. parsonsprob:: SC13_Q2
    :language: python

    Please complete the play function. 
    -----
    def play(self, agent1, agent2):
    =====
        agent1.reset()
    =====
        agent2.reset()
    =====

        for i in range(self.num_rounds):
    =====
            resp1 = agent1.respond(agent2)
    =====
            resp2 = agent2.respond(agent1)
    =====

            pay1, pay2 = self.payoffs[resp1, resp2]
    =====

            agent1.append(resp1, pay1)
    =====
            agent2.append(resp2, pay2)
    =====

        return agent1.score, agent2.score

.. parsonsprob:: SC13_Q3
    :language: python

    Please put the step function in order.
    -----
    def step(self):
        n = len(self.agents)
        fits = self.get_fitnesses()
    =====
        # see who dies
        index_dead = self.choose_dead(fits)
        num_dead = len(index_dead)
    =====
        # replace the dead with copies of the living
        replacements = self.choose_replacements(num_dead, fits)
        self.agents[index_dead] = replacements
    =====
        # update any instruments
        self.update_instruments()

