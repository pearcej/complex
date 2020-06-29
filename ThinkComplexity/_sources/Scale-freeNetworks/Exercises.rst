Exercises
---------
**Exercise 1:**  
In :ref:`Section 5.9 <5.9>` we discussed two explanations for the small world phenomenon, “weak ties” and “hubs”. Are these explanations compatible; that is, can they both be right? Which do you find more satisfying as an explanation, and why?

Is there data you could collect, or experiments you could perform, that would provide evidence in favor of one model over the other?

Choosing among competing models is the topic of Thomas Kuhn’s essay, “Objectivity, Value Judgment, and Theory Choice”, which you can read at http://thinkcomplex.com/kuhn.

What criteria does Kuhn propose for choosing among competing models? Do these criteria influence your opinion about the WS and BA models? Are there other criteria you think should be considered?

**Exercise 2:** 
NetworkX provides a function called ``powerlaw_cluster_graph`` that implements the "Holme and Kim algorithm for growing graphs with powerlaw degree distribution and approximate average clustering". Read the documentation of this function (http://thinkcomplex.com/hk) and see if you can use it to generate a graph that has the same number of nodes as the Facebook dataset, the same average degree, and the same clustering coefficient. How does the degree distribution in the model compare to the actual distribution?

**Exercise 3:**  
Data files from the Barabási and Albert paper are available from http://thinkcomplex.com/netdata. Their actor collaboration data is included in the repository for this book in a file named actor.dat.gz. The following function reads the file and builds the graph.

::

    import gzip

    def read_actor_network(filename, n=None):
        G = nx.Graph()
        with gzip.open(filename) as f:
            for i, line in enumerate(f):
                nodes = [int(x) for x in line.split()]
                G.add_edges_from(thinkcomplexity.all_pairs(nodes))
                if n and i >= n:
                    break
        return G

Compute the number of actors in the graph and the average degree. Plot the PMF of degree on a log-log scale. Also plot the CDF of degree on a log-x scale, to see the general shape of the distribution, and on a log-log scale, to see whether the tail follows a power law.

Note: The actor network is not connected, so you might want to use ``nx.connected_component_subgraphs`` to find connected subsets of the nodes.

.. dragndrop:: q1_exercises
    :match_1: WS Model|||Has characteristics of a small world network, like the data, but it has low variability in the number of neighbors from node to node, unlike the data.
    :match_2: BA Model||| Has two essential features used in this model are growth and preferential attachment.
    :match_3: Explanatory model|||is used for argument by analogy.

    Match each model to the closest description. 
