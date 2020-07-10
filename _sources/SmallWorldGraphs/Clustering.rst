Clustering
----------

.. _4.6:

The next step is to compute the **clustering coefficient**, which quantifies the tendency for the nodes to form cliques. A clique is a set of nodes that are completely connected; that is, there are edges between all pairs of nodes in the set.

Suppose a particular node, ``u``, has k neighbors. If all of the neighbors are connected to each other, there would be :math:`k(k−1)/2` edges among them. The fraction of those edges that actually exist is the local clustering coefficient for :math:`u`, denoted :math:`C_u`.

If we compute the average of :math:`C_u` over all nodes, we get the “network average clustering coefficient”, denoted :math:`C`.

Here is a function that computes it.

::

    def node_clustering(G, u):
    neighbors = G[u]
    k = len(neighbors)
    if k < 2:
        return np.nan

    possible = k * (k-1) / 2
    exist = 0
    for v, w in all_pairs(neighbors):
        if G.has_edge(v, w):
            exist +=1
    return exist / possible

Again I use ``G[u]``, which returns a dictionary with the neighbors of ``u`` as keys.

If a node has fewer than 2 neighbors, the clustering coefficient is undefined, so we return ``np.nan``, which is a special value that indicates “Not a Number”.

Otherwise we compute the number of possible edges among the neighbors, count the number of those edges that actually exist, and return the fraction that exist.

We can test the function like this:

::

    >>> lattice = make_ring_lattice(10, 4)
    >>> node_clustering(lattice, 1)
    0.5

In a ring lattice with :math:`k=4`, the clustering coefficient for each node is :math:`0.5` (if you are not convinced, take another look at :ref:`Figure 4.1 <fig_4.1>`).

Now we can compute the network average clustering coefficient like this:

::

    def clustering_coefficient(G):
    cu = [node_clustering(G, node) for node in G]
    return np.nanmean(cu)

The NumPy function ``nanmean`` computes the mean of the local clustering coefficients, ignoring any values that are ``NaN``.

We can test ``clustering_coefficient`` like this:

::
    
    >>> clustering_coefficient(lattice)
    0.5

In this graph, the local clustering coefficient for all nodes is :math:`0.5`, so the average across nodes is :math:`0.5`. Of course, we expect this value to be different for WS graphs.

.. fillintheblank:: question_4.6.1
        :casei:

        If a node has fewer than ``|blank|`` neighbors, the clustering coefficient is ``|blank|``, so we return np.nan, which is a special value that indicates ``|blank|``.

        - :2: Correct!
          :x: Try again
        - :undefined: Correct!
          :x: Try again
        - :not a number: Correct!
          :x: Try again

