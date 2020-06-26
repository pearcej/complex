Watts and Strogatz
------------------
.. _4.3:

In 1998 Duncan Watts and Steven Strogatz published a paper in *Nature*, “Collective dynamics of ‘small-world’ networks”, that proposed an explanation for the small world phenomenon. You can download it from http://thinkcomplex.com/watts.


Watts and Strogatz start with two kinds of graph that were well understood: random graphs and regular graphs. In a random graph, nodes are connected at random. In a regular graph, every node has the same number of neighbors. They consider two properties of these graphs, clustering and path length:


- Clustering is a measure of the “cliquishness” of the graph. In a graph, a **clique** is a subset of nodes that are all connected to each other; in a social network, a clique is a set of people who are all friends with each other. Watts and Strogatz defined a clustering coefficient that quantifies the likelihood that two nodes that are connected to the same node are also connected to each other.

- Path length is a measure of the average distance between two nodes, which corresponds to the degrees of separation in a social network.

Watts and Strogatz show that regular graphs have high clustering and high path lengths, whereas random graphs with the same size usually have low clustering and low path lengths. So neither of these is a good model of social networks, which combine high clustering with short path lengths.

Their goal was to create a **generative model** of a social network. A generative model tries to explain a phenomenon by modeling the process that builds or leads to the phenomenon. Watts and Strogatz proposed this process for building small-world graphs:

1. Start with a regular graph with n nodes and each node connected to k neighbors.
2. Choose a subset of the edges and “rewire” them by replacing them with random edges.

The probability that an edge is rewired is a parameter, p, that controls how random the graph is. With p=0, the graph is regular; with p=1 it is completely random.

Watts and Strogatz found that small values of p yield graphs with high clustering, like a regular graph, and low path lengths, like a random graph.

In this chapter I replicate the Watts and Strogatz experiment in the following steps:

1. We’ll start by constructing a ring lattice, which is a kind of regular graph.
2. Then we’ll rewire it as Watts and Strogatz did.
3. We’ll write a function to measure the degree of clustering and use a NetworkX function to compute path lengths.
4. Then we’ll compute the degree of clustering and path length for a range of values of p.
5. Finally, I’ll present Dijkstra’s algorithm, which computes shortest paths efficiently.