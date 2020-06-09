What’s a graph?
---------------

To most people a graph is a visual representation of a data set, like a bar chart or an EKG. That’s not what this chapter is about.

In this chapter, a graph is an abstraction used to model a system that contains discrete, interconnected elements. The elements are represented by nodes (also called vertices) and the interconnections are represented by edges.

For example, you could represent a road map with one node for each city and one edge for each road between cities. Or you could represent a social network using one node for each person, with an edge between two people if they are “friends” and no edge otherwise.

In some graphs, edges have different lengths (sometimes called “weights” or “costs”). For example, in a road map, the length of an edge might represent the distance between two cities, or the travel time, or bus fare. In a social network there might be different kinds of edges to represent different kinds of relationships: friends, business associates, etc.

Edges may be undirected, if they represent a relationship that is symmetric, or directed. In a social network, friendship is usually symmetric: if A is friends with B then B is friends with A. So you would probably represent friendship with an undirected edge. In a road map, you would probably represent a one-way street with a directed edge.

Graphs have interesting mathematical properties, and there is a branch of mathematics called graph theory that studies them.

Graphs are also useful, because there are many real world problems that can be solved using graph algorithms. For example, Dijkstra’s shortest path algorithm is an efficient way to find the shortest path from a node to all other nodes in a graph. A path is a sequence of nodes with an edge between each consecutive pair.

Sometimes the connection between a real world problem and a graph algorithm is obvious. In the road map example, it is not hard to imagine using a shortest path algorithm to find the route between two cities that minimizes distance (or time, or cost).

In other cases it takes more effort to represent a problem in a form that can be solved with a graph algorithm, and then interpret the solution.

For example, a complex system of radioactive decay can be represented by a graph with one node for each nuclide (type of atom) and an edge between two nuclides if one can decay into the other. A path in this graph represents a decay chain. See http://en.wikipedia.org/wiki/Radioactive_decay.

The rate of decay between two nuclides is characterized by a decay constant, λ, measured in becquerels (Bq) or decay events per second. You might be more familiar with half-life, t1/2, which is the expected time until half of a sample decays. You can convert from one characterization to the other using the relation t1/2 = ln2 / λ.

In our best current model of physics, nuclear decay is a fundamentally random process, so it is impossible to predict when an atom will decay. However, given λ, the probability that an atom decays during a short time interval dt is λ dt.

In a graph with multiple decay chains, the probability of a given path is the product of the probabilities of each decay process in the path.

Now suppose you want to find the decay chain with the highest probability. You could do it by assigning each edge a “length” of −logλ and using a shortest path algorithm. Why? Because the shortest path algorithm adds up the lengths of the edges, and adding up log-probabilities is the same as multiplying probabilities. Also, because the logarithms are negated, the smallest sum corresponds to the largest probability. So the shortest path corresponds to the most likely decay chain.

This is an example of a common and useful process in applying graph algorithms:

Reduce
a real-world problem to an instance of a graph problem.
Apply
a graph algorithm to compute the result efficiently.
Interpret
the result of the computation in terms of a solution to the original problem.
We will see other examples of this process soon.

Exercise 1  
Read the Wikipedia page about graphs at http://en.wikipedia.org/wiki/Graph_(mathematics) and answer the following questions:

1. What is a simple graph? In the rest of this section, we will be assuming that all graphs are simple graphs. This is a common assumption for many graph algorithms—so common it is often unstated.
2. What is a regular graph? What is a complete graph? Prove that a complete graph is regular.
3. What is a path? What is a cycle?
4. What is a forest? What is a tree? Note: a graph is connected if there is a path from every node to every other node.