Self Check
------------

.. fillintheblank:: SC4_Q1
        :casei:

        |blank| is a graph with n nodes, the nodes can be arranged in a circle with each node connected to the k nearest neighbors.
 
        - :ring lattice: Correct.
          :WS graphs: Incorrect. WS graphs in the book refer to the Watts-Strogatz model that is based on a random graph generation model which produces graphs with small-world properties.
          :Regular graph: Incorrect. A regular graph is a graph where each node has the same number of neighbors. This graph is a kind of regular graph. Please try again.
          :x: Try again.

.. mchoice:: SC4_Q2
    :answer_a: Breadth-first search (BFS)
    :answer_b: Depth-first search (DFS)
    :answer_c: Dijkstra’s algorithm
    :answer_d: Bellman-Ford Algorithm
    :correct: a,c
    :feedback_a: Good Job!
    :feedback_b: Incorrect, DFS is not used for computing the shortest path between  nodes. Please try again.
    :feedback_c: Correct!
    :feedback_d: Incorrect, Bellman-Ford is not used. Please try again

    Which of the below graph algorithms are used for computing the shortest path between nodes. Select multiple choices.

.. dragndrop:: SC4_Q3
    :match_1: 1|||Rewire some of the edges of the ring lattice.
    :match_2: 2|||Quantify the tendency for the nodes to form cliques.
    :match_3: 3|||Compute the average length of the shortest path between each pair of nodes.
    :match_4: 4|||You are ready to replicate the WS experiment. 

    Match the following to the order that they need to be in to build a Watts-Strogatz (WS) graph. 