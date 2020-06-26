Introduction
------------
Many networks in the real world, including social networks, have the “small world property”, which is that the average distance between nodes, measured in number of edges on the shortest path, is much smaller than expected.

In this chapter, I present Stanley Milgram’s famous Small World Experiment, which was the first demonstration of the small world property in a real social network. Then we’ll consider Watts-Strogatz graphs, which are intended as a model of small world graphs. I’ll replicate the experiment Watts and Strogatz performed and explain what it is intended to show.

Along the way, we’ll see two new graph algorithms: breadth-first search (BFS) and Dijkstra’s algorithm for computing the shortest path between nodes in a graph.

The code for this chapter is in chap03.ipynb in the repository for this book. More information about working with the code is in :ref:`Section 1.4<1.4>`.