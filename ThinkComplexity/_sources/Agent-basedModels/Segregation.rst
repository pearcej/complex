.. _seg_1:

Segregation
------------



.. figure:: Figures/figure_10.1.png
    :align: center
    :alt: "Figure 10.1: Schelling’s segregation model with n=100, initial condition (left), after 2 steps (middle), and after 10 steps (right)."

    Figure 10.1: Schelling’s segregation model with n=100, initial condition (left), after 2 steps (middle), and after 10 steps (right).

Now let’s see what happens when we run the model. I’ll start with ``n=100`` and ``p=0.3``, and run for 10 steps.

::

    grid = Schelling(n=100, p=0.3)
    for i in range(10):
        grid.step()

:ref:`Figure 10.1 <seg_1>` shows the initial configuration (left), the state of the simulation after 2 steps (middle), and the state after 10 steps (right).

Clusters form almost immediately and grow quickly, until most agents live in highly-segregated neighborhoods.

As the simulation runs, we can compute the degree of segregation, which is the average, across agents, of the fraction of neighbors who are the same color as the agent:

::

    np.nanmean(frac_same)

In :ref:`Figure 10.1 <seg_1>`, the average fraction of similar neighbors is 50% in the initial configuration, 65% after two steps, and 76% after 10 steps!

Remember that when ``p=0.3`` the agents would be happy if 3 of 8 neighbors were their own color, but they end up living in neighborhoods where 6 or 7 of their neighbors are their own color, typically.

.. _seg_2:

.. figure:: Figures/figure_10.2.png
    :align: center
    :alt: "Figure 10.2: Degree of segregation in Schelling’s model, over time, for a range of p."

    Figure 10.2: Degree of segregation in Schelling’s model, over time, for a range of p.


:ref:`Figure 10.2 <seg_2>` shows how the degree of segregation increases and where it levels off for several values of ``p``. When ``p=0.4``, the degree of segregation in steady state is about 82%, and a majority of agents have no neighbors with a different color.

These results are surprising to many people, and they make a striking example of the unpredictable relationship between individual decisions and system behavior.

.. fillintheblank:: 1_10.2

    The average fraction of similar neighbors is |blank| % in the initial configuration, |blank| % after two steps, and |blank| % after 10 steps!

    - :50: Correct!
      :x: Incorrect, please refer back to the text.
    - :65: Correct!
      :x: Incorrect, please refer back to the text.
    - :75: Correct!
      :x: Incorrect, please refer back to the text.

.. mchoice:: q_10.3
   :answer_a: 30%
   :answer_b: 82%
   :answer_c: 76%
   :answer_d: 50%
   :correct: b
   :feedback_a: Sorry but that is what percentage of agents will be unhappy if p=0.3.
   :feedback_b: Correct!
   :feedback_c: Sorry but that was the percentage from 10 steps into the p=0.3 example above.
   :feedback_d: Sorry but that was the initial configuration of the p=0.3 example above.

   When p=0.4 what is the approximate degree of segregation in a steady state?