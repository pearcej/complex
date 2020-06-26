
.. _3.6:

Connected Graphs
----------------

A graph is **connected** if there is a path from every node to every other node (see http://thinkcomplex.com/conn).

For many applications involving graphs, it is useful to check whether a graph is connected. Fortunately, there is a simple algorithm that does it.

You can start at any node and check whether you can reach all other nodes. If you can reach a node, v, you can reach any of the neighbors of v, which are the nodes connected to v by an edge.

The Graph class provides a method called neighbors that returns a list of **neighbors** for a given node. For example, in the complete graph we generated in the previous section:

::

    >>> complete.neighbors(0)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

Suppose we start at node s. We can mark s as “seen” and mark its neighbors. Then we mark the neighbor’s neighbors, and their neighbors, and so on, until we can’t reach any more nodes. If all nodes are seen, the graph is connected.

Here’s what that looks like in Python:

::

    def reachable_nodes(G, start):
    seen = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.neighbors(node))
    return seen

``reachable_nodes`` takes a ``Graph`` and a starting node, ``start``, and returns the set of nodes that can be reached from ``start``.

Initially the ``set``, ``seen``, is empty, and we create a list called ``stack`` that keeps track of nodes we have discovered but not yet processed. Initially the stack contains a single node, ``start``.

Now, each time through the loop, we:

1. Remove one node from the stack.
2. If the node is already in ``seen``, we go back to Step 1.
3. Otherwise, we add the node to ``seen`` and add its neighbors to the stack.

When the stack is empty, we can’t reach any more nodes, so we break out of the loop and return ``seen``.

As an example, we can find all nodes in the complete graph that are reachable from node 0:

::

    >>> reachable_nodes(complete, 0)
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

Initially, the stack contains node 0 and ``seen`` is empty. The first time through the loop, node 0 is added to ``seen`` and all the other nodes are added to the stack (since they are all neighbors of node 0).

The next time through the loop, ``pop`` returns the last element in the stack, which is node 9. So node 9 gets added to ``seen`` and its neighbors get added to the stack.

Notice that the same node can appear more than once in the stack; in fact, a node with k neighbors will be added to the stack k times. Later, we will look for ways to make this algorithm more efficient.

We can use ``reachable_nodes`` to write ``is_connected``:

::

    def is_connected(G):
    start = next(iter(G))
    reachable = reachable_nodes(G, start)
    return len(reachable) == len(G)

``is_connected`` chooses a starting node by making a node iterator and choosing the first element. Then it uses ``reachable`` to get the set of nodes that can be reached from ``start``. If the size of this set is the same as the size of the graph, that means we can reach all nodes, which means the graph is connected.

A complete graph is, not surprisingly, connected:

::
    
    >>> is_connected(complete)
    True

In the next section we will generate ER graphs and check whether they are connected.

.. shortanswer:: short-3.6

   The author says that “A complete graph is, not surprisingly, connected”, why is this?