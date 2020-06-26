Exercises
---------
Exercise 1  
In a ring lattice, every node has the same number of neighbors. The number of neighbors is called the **degree** of the node, and a graph where all nodes have the same degree is called a **regular graph**.

All ring lattices are regular, but not all regular graphs are ring lattices. In particular, if k is odd, we can’t construct a ring lattice, but we might be able to construct a regular graph.

Write a function called make_regular_graph that takes n and k and returns a regular graph that contains n nodes, where every node has k neighbors. If it’s not possible to make a regular graph with the given values of n and k, the function should raise a ValueError.

Exercise 2  
My implementation of ``reachable_nodes_bfs`` is efficient in the sense that it is in O(n + m), but it incurs a lot of overhead adding nodes to the queue and removing them. NetworkX provides a simple, fast implementation of BFS, available from the NetworkX repository on GitHub at http://thinkcomplex.com/connx.

Here is a version I modified to return a set of nodes:

::

    def plain_bfs(G, start):
    seen = set()
    nextlevel = {start}
    while nextlevel:
        thislevel = nextlevel
        nextlevel = set()
        for v in thislevel:
            if v not in seen:
                seen.add(v)
                nextlevel.update(G[v])
    return seen

Compare this function to ``reachable_nodes_bfs`` and see which is faster. Then see if you can modify this function to implement a faster version of ``shortest_path_dijkstra``.

Exercise 3  
The following implementation of BFS contains two performance errors. What are they? What is the actual order of growth for this algorithm?

::

    def bfs(G, start):
    visited = set()
    queue = [start]
    while len(queue):
        curr_node = queue.pop(0)    # Dequeue
        visited.add(curr_node)

        # Enqueue non-visited and non-enqueued children
        queue.extend(c for c in G[curr_node]
                     if c not in visited and c not in queue)
    return visited

Exercise 4   In :ref:`Section 4.11 <4.11>`, I claimed that Dijkstra’s algorithm does not work unless it uses BFS. Write a version of ``shortest_path_dijkstra`` that uses DFS and test it on a few examples to see what goes wrong.
Exercise 5  
A natural question about the Watts and Strogatz paper is whether the small world phenomenon is specific to their generative model or whether other similar models yield the same qualitative result (high clustering and low path lengths).

To answer this question, choose a variation of the Watts and Strogatz model and repeat the experiment. There are two kinds of variation you might consider:

- Instead of starting with a regular graph, start with another graph with high clustering. For example, you could put nodes at random locations in a 2-D space and connect each node to its nearest k neighbors.
- Experiment with different kinds of rewiring.

If a range of similar models yield similar behavior, we say that the results of the paper are **robust**.

Exercise 6  
Dijkstra’s algorithm solves the “single source shortest path” problem, but to compute the characteristic path length of a graph, we actually want to solve the “all pairs shortest path” problem.

Of course, one option is to run Dijkstra’s algorithm n times, once for each starting node. And for some applications, that’s probably good enough. But there are are more efficient alternatives.

Find an algorithm for the all-pairs shortest path problem and implement it. See http://thinkcomplex.com/short.

Compare the run time of your implementation with running Dijkstra’s algorithm n times. Which algorithm is better in theory? Which is better in practice? Which one does NetworkX use?
