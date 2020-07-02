Generating BA graphs
--------------------
In the previous sections we used a NetworkX function to generate BA graphs; now let’s see how it works. Here is a version of ``barabasi_albert_graph``, with some changes I made to make it easier to read:

::

    def barabasi_albert_graph(n, k):

    G = nx.empty_graph(k)
    targets = list(range(k))
    repeated_nodes = []

    for source in range(k, n):
        G.add_edges_from(zip([source]*k, targets))

        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * k)

        targets = _random_subset(repeated_nodes, k)

    return G

The parameters are ``n``, the number of nodes we want, and ``k``, the number of edges each new node gets (which will turn out to be the average number of edges per node).

We start with a graph that has ``k`` nodes and no edges. Then we initialize two variables:

``targets``:
The list of ``k`` nodes that will be connected to the next node. Initially ``targets`` contains the original ``k`` nodes; later it will contain a random subset of nodes.

``repeated_nodes``:
A list of existing nodes where each node appears once for every edge it is connected to. When we select from ``repeated_nodes``, the probability of selecting any node is proportional to the number of edges it has.

Each time through the loop, we add edges from the source to each node in ``targets``. Then we update ``repeated_nodes`` by adding each target once and the new node ``k`` times.

Finally, we choose a subset of the nodes to be targets for the next iteration. Here’s the definition of ``_random_subset``:

::

    def _random_subset(repeated_nodes, k):
    targets = set()
    while len(targets) < k:
        x = random.choice(repeated_nodes)
        targets.add(x)
    return targets

Each time through the loop, ``_random_subset`` chooses from ``repeated_nodes`` and adds the chosen node to ``targets``. Because ``targets`` is a set, it automatically discards duplicates, so the loop only exits when we have selected ``k`` different nodes.