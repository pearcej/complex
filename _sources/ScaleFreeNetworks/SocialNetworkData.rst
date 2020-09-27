..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _SFN_2:

Social Network Data
-------------------

Watts-Strogatz graphs are intended to model networks in the natural and social sciences. In their original paper, Watts and Strogatz looked at the network of film actors (connected if they have appeared in a movie together); the electrical power grid in the western United States; and the network of neurons in the brain of the roundworm :math:`C`. *elegans*. They found that all of these networks had the high connectivity and low path lengths characteristic of small world graphs.

In this section we’ll perform the same analysis with a different dataset, a set of Facebook users and their friends. If you are not familiar with Facebook, users who are connected to each other are called “friends”, regardless of the nature of their relationship in the real world.

I’ll use data from the Stanford Network Analysis Project (SNAP), which shares large datasets from online social networks and other sources. Specifically, I’ll use their Facebook data, which includes 4039 users and 88,234 friend relationships among them. This dataset is in the repository for this book, but it is also available from the SNAP website.

The data file contains one line per edge, with users identified by integers from 0 to 4038. Here’s the code that reads the file:

::

    def read_graph(filename):
        G = nx.Graph()
        array = np.loadtxt(filename, dtype=int)
        G.add_edges_from(array)
        return G

NumPy provides a function called ``loadtext`` that reads the given file and returns the contents as a NumPy array. The parameter ``dtype`` indicates that the “data type” of the array is int.

Then we use ``add_edges_from`` to iterate the rows of the array and make edges. Here are the results:

::

    >>> fb = read_graph('facebook_combined.txt.gz')
    >>> n = len(fb)
    >>> m = len(fb.edges())
    >>> n, m
    (4039, 88234)

The node and edge counts are consistent with the documentation of the dataset.

Now we can check whether this dataset has the characteristics of a small world graph: high clustering and low path lengths.

In :ref:`Section 5.6 <SWG_6>` we wrote a function to compute the network average clustering coefficient. NetworkX provides a function called ``average_clustering``, which does the same thing a little faster.

But for larger graphs, they are both too slow, taking time proportional to :math:`n k^2`, where ``n`` is the number of nodes and ``k`` is the number of neighbors each node is connected to.

Fortunately, NetworkX provides a function that estimates the clustering coefficient by random sampling. You can invoke it like this:

::

    from networkx.algorithms.approximation import average_clustering
        average_clustering(G, trials=1000)

The following function does something similar for path lengths.
::

    def sample_path_lengths(G, nodes=None, trials=1000):
        if nodes is None:
            nodes = list(G)
        else:
            nodes = list(nodes)

        pairs = np.random.choice(nodes, (trials, 2))
        lengths = [nx.shortest_path_length(G, *pair)
                for pair in pairs]
        return lengths

``G`` is a graph, ``nodes`` is the list of nodes to sample from, and ``trials`` is the number of random paths to sample. If ``nodes`` is None, we sample from the entire graph.

``pairs`` is a NumPy array of randomly chosen nodes with one row for each trial and two columns.

The list comprehension enumerates the rows in the array and computes the shortest distance between each pair of nodes. The result is a list of path lengths.

``estimate_path_length`` generates a list of random path lengths and returns their mean:

::

    def estimate_path_length(G, nodes=None, trials=1000):
        return np.mean(sample_path_lengths(G, nodes, trials))

I’ll use ``average_clustering`` to compute ``C``:
::

    C = average_clustering(fb)

And ``estimate_path_lengths`` to compute ``L``:

::

    L = estimate_path_lengths(fb)

The clustering coefficient is about 0.61, which is high, as we expect if this network has the small world property.

And the average path is 3.7, which is quite short in a network of more than 4000 users. It’s a small world after all.

Now let’s see if we can construct a WS graph that has the same characteristics as this network.

.. dragndrop:: Q1_5.2
    :match_1: loadtext|||A function that reads the given file and returns the contents as a NumPy array.
    :match_2: average_clustering|||Function provided by networkx that computes the network average clustering coefficient.
    :match_3: n|||The number of nodes.
    :match_4: K|||The number of neighbors each node is connected to.
    :match_5: G|||A graph.
    :match_6: nodes|||The list of nodes to sample from and if this is None, we sample from the entire graph.
    :match_7: Trails|||Is the number of random paths to sample.
    :match_8: pairs|||A NumPy array of randomly chosen nodes with one row for each trial and two columns.
    :match_9: estimate_path_length|||Function that  generates a list of random path lengths and returns their mean.
    :match_10: L|||Is computed using estimate_path_lengths.
    :match_11: C|||Is computed using average_clustering.
