..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Self Check
-----------

.. fillintheblank:: SC9_Q1
    :casei:

    |blank| means that from any initial condition, the system moves toward a |blank| state, and stays there, without external control.

    - :Self-organized: Correct.
      :x: Incorrect.
    - :critical: Correct.
      :x: Incorrect.

.. parsonsprob:: SC9_Q2
    :language: python

    Please put the step method that finds all cells above k and topples them.
    -----
    def step(self, K=3):
    =====
        toppling = self.array > K
        =====
        num_toppled = np.sum(toppling)
        =====
        c = correlate2d(toppling, self.kernel, mode='same')
        =====
        self.array += c
        =====
        return num_toppled

.. fillintheblank:: SC9_Q3
    :casei:

    A |blank| model describes a system by describing its parts and their interactions. |blank| models are more focused on similarities between systems and less interested in analogous parts.

    - :reductionist: Correct.
      :holistic: Incorrect, holistic models are more focused on similarities between systems and less interested in analogous parts.
      :x: Incorrect.
    - :holistic: Correct.
      :reductionist: Incorrect, reductionists models describe a system by describing its parts and their interactions.
      :x: Incorrect.

.. fillintheblank:: SC9_Q4
    :casei:

    The |blank| cause of an avalanch in a sand pile is a grain of sand and the |blank| cause is the structe and dynamics of the systems as a whole.

    - :proximate: Correct.
      :ultimate: Incorrect, the ultimate cause is the structure and dynamics as a whole.
      :x: Incorrect.
    - :ultimate: Correct.
      :proximate: Incorrect, the proximate cause is the grain of sand that starts the avalanche.
      :x: Incorrect.
