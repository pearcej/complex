Exercises
---------
The code for this chapter is in chap02.ipynb, which is a Jupyter notebook in the repository for this book. For more information about working with this code, see Section ??.

Exercise 1   Launch chap02.ipynb and run the code. There are a few short exercises embedded in the notebook that you might want to try.

Exercise 2   In Section ?? we analyzed the performance of reachable_nodes and classified it in O(n + m), where n is the number of nodes and m is the number of edges. Continuing the analysis, what is the order of growth for ``is_connected``?

::

    def is_connected(G):
        start = list(G)[0]
        reachable = reachable_nodes(G, start)
        return len(reachable) == len(G)

Exercise 3   In my implementation of ``reachable_nodes``, you might be bothered by the apparent inefficiency of adding all neighbors to the stack without checking whether they are already in ``seen``. Write a version of this function that checks the neighbors before adding them to the stack. Does this “optimization” change the order of growth? Does it make the function faster?

Exercise 4  
There are actually two kinds of ER graphs. The one we generated in this chapter, G(n, p), is characterized by two parameters, the number of nodes and the probability of an edge between nodes.

An alternative definition, denoted G(n, m), is also characterized by two parameters: the number of nodes, n, and the number of edges, m. Under this definition, the number of edges is fixed, but their location is random.

Repeat the experiments we did in this chapter using this alternative definition. Here are a few suggestions for how to proceed:

1. Write a function called ``m_pairs`` that takes a list of nodes and the number of edges, m, and returns a random selection of m edges. A simple way to do that is to generate a list of all possible edges and use random.sample.

2. Write a function called ``make_m_graph`` that takes n and m and returns a random graph with n nodes and m edges.

3. Make a version of ``prob_connected`` that uses ``make_m_graph`` instead of ``make_random_graph``.

4. Compute the probability of connectivity for a range of values of m.

How do the results of this experiment compare to the results using the first type of ER graph?