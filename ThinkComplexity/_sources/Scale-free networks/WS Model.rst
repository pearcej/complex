WS models
---------
In the Facebook dataset, the average number of edges per node is about 22. Since each edge is connected to two nodes, the average degree is twice the number of edges per node:
::

    >>> k = int(round(2*m/n))
    >>> k
    44

We can make a WS graph with n=4039 and k=44. When p=0, we get a ring lattice.

::
    lattice = nx.watts_strogatz_graph(n, k, 0)

In this graph, clustering is high: C is 0.73, compared to 0.61 in the dataset. But L is 46, much higher than in the dataset!

With p=1 we get a random graph:

::
    random_graph = nx.watts_strogatz_graph(n, k, 1)

In the random graph, L is 2.6, even shorter than in the dataset (3.7), but C is only 0.011, so that’s no good.

By trial and error, we find that when p=0.05 we get a WS graph with high clustering and low path length:

::

    ws = nx.watts_strogatz_graph(n, k, 0.05, seed=15)

In this graph C is 0.63, a bit higher than in the dataset, and L is 3.2, a bit lower than in the dataset. So this graph models the small world characteristics of the dataset well.

So far, so good.




