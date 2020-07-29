Random Graphs
--------------

.. _3.4:

A **random graph** is just what it sounds like: a graph with nodes and edges generated at random. Of course, there are many random processes that can generate graphs, so there are many kinds of random graphs.


One of the more interesting kinds is the Erdős-Rényi model, studied by Paul Erdős and Alfréd Rényi in the 1960s.


An **Erdős-Rényi graph** (**ER graph**) is characterized by two parameters: ``n`` is the number of nodes and ``p`` is the probability that there is an edge between any two nodes.

Erdős and Rényi studied the properties of these random graphs; one of their surprising results is the existence of abrupt changes in the properties of random graphs as random edges are added.


One of the properties that displays this kind of transition is connectivity. An **undirected graph** is connected if there is a path from every node to every other node.


In an ER graph, the probability that the graph is **connected** is very low when :math:`p` is small and nearly 1 when :math:`p` is large. Between these two regimes, there is a rapid transition at a particular value of :math:`p`, denoted :math:`p*`.

Erdős and Rényi showed that this critical value is :math:`p* = (lnn) / n`, where :math:`n` is the number of nodes. A random graph, :math:`G(n, p)`, is unlikely to be connected if :math:`p < p*` and very likely to be connected if :math:`p > p*`.


To test this claim, we’ll develop algorithms to generate random graphs and check whether they are connected.

.. mchoice:: question3_1
   :answer_a: True
   :answer_b: False
   :correct: a   
   :feedback_a: Correct! The value of p is greater than p*
   :feedback_b: Not quite. In an ER graph when p is higher than p* this leads to a greater possiblity of the graph being connected.

   Given that an Erdős-Rényi graph (ER graph) a has a :math:`p* = .6` and a :math:`p = .7` it is more likely to be connected.

