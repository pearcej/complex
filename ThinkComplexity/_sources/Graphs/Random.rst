Random Graphs
--------------

.. _3.4:

A random graph is just what it sounds like: a graph with nodes and edges generated at random. Of course, there are many random processes that can generate graphs, so there are many kinds of random graphs.


One of the more interesting kinds is the Erdős-Rényi model, studied by Paul Erdős and Alfréd Rényi in the 1960s.


An Erdős-Rényi graph (ER graph) is characterized by two parameters: n is the number of nodes and p is the probability that there is an edge between any two nodes. See http://thinkcomplex.com/er.


Erdős and Rényi studied the properties of these random graphs; one of their surprising results is the existence of abrupt changes in the properties of random graphs as random edges are added.


One of the properties that displays this kind of transition is connectivity. An undirected graph is connected if there is a path from every node to every other node.


In an ER graph, the probability that the graph is **connected** is very low when p is small and nearly 1 when p is large. Between these two regimes, there is a rapid transition at a particular value of p, denoted p*.

Erdős and Rényi showed that this critical value is p* = (lnn) / n, where n is the number of nodes. A random graph, G(n, p), is unlikely to be connected if p < p* and very likely to be connected if p > p*.


To test this claim, we’ll develop algorithms to generate random graphs and check whether they are connected.

.. mchoice:: question3_1
   :answer_a: True
   :answer_b: False
   :correct: a   
   :feedback_a: Correct! The value of p is greater than p*
   :feedback_b: Not quite. Look at the two values and see how they compare

   Given that a graph a has a p* = .6 and a p = .7 is it more likely to be connected.

