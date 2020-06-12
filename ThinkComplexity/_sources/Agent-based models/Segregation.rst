Segregation
------------

Figure 9.1::

Now let’s see what happens when we run the model. I’ll start with n=100 and p=0.3, and run for 10 steps.

::

    grid = Schelling(n=100, p=0.3)
    for i in range(10):
        grid.step()

Figure ?? shows the initial configuration (left), the state of the simulation after 2 steps (middle), and the state after 10 steps (right).

Clusters form almost immediately and grow quickly, until most agents live in highly-segregated neighborhoods.

As the simulation runs, we can compute the degree of segregation, which is the average, across agents, of the fraction of neighbors who are the same color as the agent:

::

    np.nanmean(frac_same)

In Figure ??, the average fraction of similar neighbors is 50% in the initial configuration, 65% after two steps, and 76% after 10 steps!

Remember that when p=0.3 the agents would be happy if 3 of 8 neighbors were their own color, but they end up living in neighborhoods where 6 or 7 of their neighbors are their own color, typically.

Figure 9.2::

Figure ?? shows how the degree of segregation increases and where it levels off for several values of p. When p=0.4, the degree of segregation in steady state is about 82%, and a majority of agents have no neighbors with a different color.

These results are surprising to many people, and they make a striking example of the unpredictable relationship between individual decisions and system behavior.

