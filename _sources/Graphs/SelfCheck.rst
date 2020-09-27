..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Self Check
----------

.. figure:: Figures/SELF_CHECK_FIG.png
   :align: center
   :alt: "Graph of Friend Network"

   A Graphical represention of a Friend Network

.. mchoice:: SC_Q1
   :answer_a: Instagram
   :answer_b: Twitter
   :answer_c: Reddit
   :answer_d: Facebook
   :correct: d
   :feedback_a: This is incorrect due to the graph not being directed.
   :feedback_b: This is incorrect due to the graph not being directed.
   :feedback_c: This is incorrect due to the graph not being directed.
   :feedback_d: Correct, because the Graph is undirected.

   Based on the graph above what social media platform would the user be using?



.. dragndrop:: sc_match
   :match_1: G|||This variable is a DiGraph object that contains no nodes and no edges.
   :match_2: add_node|||This method adds nodes.
   :match_3: nodes|||This method gets a list of nodes.
   :match_4: Nodeview|||This class can be used in a for loop or it can make a list.
   :match_5: Edges|||This method gets a list of edges.
   :match_6: Draw_circular|||This method arranges the nodes in a circle and connects them with edges.

   Match the correct NetworkX code piece to the correct  description.


.. parsonsprob:: sc_parsons
   :language: python

   Please construct def complete_graph:
   -----
   def make_complete_graph(n):
   =====
       G = nx.Graph()
       =====
       nodes = range(n)
       =====
       G.add_nodes_from(nodes)
       =====
       G.add_edges_from(all_pairs(nodes))
       =====
       return G


.. fillintheblank:: blank_SC
   :casei:

   The order of growth for graph algorithms is usually expressed as a function of n, |blank| (nodes), and m, |blank|.

   - :the number of vertices: Correct!
     :the number of edges: Close, but this refers to something else.
     :number of vertices: Close, add the to the beginning of your statement
     :x: Sorry you are incorrect, try again and checkout section 3.9.

   - :the number of edges: Correct!
     :the number of vertices: Close, but this refers to something else.
     :number of edges: Close, add the to the beginning of your statement
     :x: Sorry you are incorrect, Try again and checkout section 3.9.
