.. _3.9:

Analysis of Graph Algorithms
----------------------------
Earlier in this chapter I presented an algorithm for checking whether a graph is connected; in the next few chapters, we will see other graph algorithms. Along the way, we will analyze the performance of those algorithms, figuring out how their run times grow as the size of the graphs increases.

If you are not already familiar with analysis of algorithms, you might want to read *Appendix B of Think Python, 2nd Edition*, at http://thinkcomplex.com/tp2.

The order of growth for graph algorithms is usually expressed as a function of :math:`n`, the number of vertices (nodes), and :math:`m`, the number of edges.

As an example, let’s analyze reachable_nodes from :ref:`Section 3.6 <3.6>`

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

Each time through the loop, we pop a node off the stack; by default, pop removes and returns the last element of a list, which is a constant time operation.

Next we check whether the node is in ``seen``, which is a set, so checking membership is constant time.

If the node is not already in ``seen``, we add it, which is constant time, and then add the neighbors to the stack, which is linear in the number of neighbors.

To express the run time in terms of :math:`n` and :math:`m`, we can add up the total number of times each node is added to ``seen`` and ``stack``.

Each node is only added to ``seen`` once, so the total number of additions is n.

But nodes might be added to ``stack`` many times, depending on how many neighbors they have. If a node has k neighbors, it is added to ``stack`` :math:`k` times. Of course, if it has :math:`k` neighbors, that means it is connected to :math:`k` edges.

So the total number of additions to ``stack`` is the total number of edges, m, doubled because we consider every edge twice.

Therefore, the order of growth for this function is :math:`O(n + m)`, which is a convenient way to say that the run time grows in proportion to either n or m, whichever is bigger.

If we know the relationship between :math:`n` and :math:`m`, we can simplify this expression. For example, in a complete graph the number of edges is :math:`n(n−1)/2`, which is in :math:`O(n^2)`. So for a complete graph, ``reachable_nodes`` is quadratic in :math:`n`.

.. mchoice:: question3_9
   :answer_a: True
   :answer_b: False
   :correct: a   
   :feedback_a: Correct! If a node has k neighbors, it is added to stack k times.
   :feedback_b: Incorrect

   It is possible for a node to be added to the stack multiple times depending on the amount of neighbors the node has

























