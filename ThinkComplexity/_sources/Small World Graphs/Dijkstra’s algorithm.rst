Dijkstra’s algorithm
--------------------
Edsger W. Dijkstra was a Dutch computer scientist who invented an efficient shortest-path algorithm (see http://thinkcomplex.com/dijk). He also invented the semaphore, which is a data structure used to coordinate programs that communicate with each other (see http://thinkcomplex.com/sem and Downey, The Little Book of Semaphores).

Dijkstra is famous (and notorious) as the author of a series of essays on computer science. Some, like “A Case against the GO TO Statement”, had a profound effect on programming practice. Others, like “On the Cruelty of Really Teaching Computing Science”, are entertaining in their cantankerousness, but less effective.

Dijkstra’s algorithm solves the “single source shortest path problem”, which means that it finds the minimum distance from a given “source” node to every other node in the graph (or at least every connected node).

I’ll present a simplified version of the algorithm that considers all edges the same length. The more general version works with any non-negative edge lengths.

The simplified version is similar to the breadth-first search in the previous section except that we replace the set called seen with a dictionary called dist, which maps from each node to its distance from the source:

::

    def shortest_path_dijkstra(G, source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        new_dist = dist[node] + 1

        neighbors = set(G[node]).difference(dist)
        for n in neighbors:
            dist[n] = new_dist

        queue.extend(neighbors)
    return dist

Here’s how it works:

- Initially, queue contains a single element, source, and dist maps from source to distance 0 (which is the distance from source to itself).
- Each time through the loop, we use popleft to select the next node in the queue.
- Next we find all neighbors of node that are not already in dist.
- Since the distance from source to node is dist[node], the distance to any of the undiscovered neighbors is dist[node]+1.
- For each neighbor, we add an entry to dist, then we add the neighbors to the queue.

This algorithm only works if we use BFS, not DFS. To see why, consider this:

- The first time through the loop node is source, and new_dist is 1. So the neighbors of source get distance 1 and they go in the queue.
- When we process the neighbors of source, all of their neighbors get distance 2. We know that none of them can have distance 1, because if they did, we would have discovered them during the first iteration.
- Similarly, when we process the nodes with distance 2, we give their neighbors distance 3. We know that none of them can have distance 1 or 2, because if they did, we would have discovered them during a previous iteration.

And so on. If you are familiar with proof by induction, you can see where this is going.

But this argument only works if we process all nodes with distance 1 before we start processing nodes with distance 2, and so on. And that’s exactly what BFS does.

In the exercises at the end of this chapter, you’ll write a version of Dijkstra’s algorithm using DFS, so you’ll have a chance to see what goes wrong.