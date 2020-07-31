.. _SWG_7:

Shortest Path Lengths
----------------------

The next step is to compute the characteristic path length, :math:`L`, which is the average length of the shortest path between each pair of nodes. To compute it, I’ll start with a function provided by NetworkX, shortest_path_length. I’ll use it to replicate the Watts and Strogatz experiment, then I’ll explain how it works.

Here’s a function that takes a graph and returns a list of shortest path lengths, one for each pair of nodes.

::

    def path_lengths(G):
    length_map = nx.shortest_path_length(G)
    lengths = [length_map[u][v] for u, v in all_pairs(G)]
    return lengths

The return value from ``nx.shortest_path_length`` is a dictionary of dictionaries. The outer dictionary maps from each node, ``u``, to a dictionary that maps from each node, ``v``, to the length of the shortest path from ``u`` to ``v``.

With the list of lengths from ``path_lengths``, we can compute :math:`L` like this:

::

    def characteristic_path_length(G):
    return np.mean(path_lengths(G))

And we can test it with a small ring lattice:

::

    >>> lattice = make_ring_lattice(3, 2)
    >>> characteristic_path_length(lattice)
    1.0

In this example, all 3 nodes are connected to each other, so the mean path length is :math:`1`.