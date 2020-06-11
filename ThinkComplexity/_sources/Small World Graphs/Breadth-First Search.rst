Breadth-First Search
--------------------
When we computed shortest paths, we used a function provided by NetworkX, but I have not explained how it works. To do that, I’ll start with breadth-first search, which is the basis of Dijkstra’s algorithm for computing shortest paths.

In Section ?? I presented reachable_nodes, which finds all the nodes that can be reached from a given starting node:

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

I didn’t say so at the time, but reachable_nodes performs a depth-first search (DFS). Now we’ll modify it to perform breadth-first search (BFS).

To understand the difference, imagine you are exploring a castle. You start in a room with three doors marked A, B, and C. You open door C and discover another room, with doors marked D, E, and F.

Which door do you open next? If you are feeling adventurous, you might want to go deeper into the castle and choose D, E, or F. That would be a depth-first search.

But if you wanted to be more systematic, you might go back and explore A and B before D, E, and F. That would be a breadth-first search.

In reachable_nodes, we use the list method pop to choose the next node to “explore”. By default, pop returns the last element of the list, which is the last one we added. In the example, that would be door F.

If we want to perform a BFS instead, the simplest solution is to pop the first element of the list:

::

    node = stack.pop(0)

That works, but it is slow. In Python, popping the last element of a list takes constant time, but popping the first element is linear in the length of the list. In the worst case, the length of the stack is O(n), which makes this implementation of BFS O(nm), which is much worse than what it should be, O(n + m).

We can solve this problem with a double-ended queue, also known as a deque. The important feature of a deque is that you can add and remove elements from the beginning or end in constant time. To see how it is implemented, see http://thinkcomplex.com/deque.

Python provides a deque in the collections module, so we can import it like this:

::

    from collections import deque

And we can use it to write an efficient BFS:

::

    def reachable_nodes_bfs(G, start):
    seen = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in seen:
            seen.add(node)
            queue.extend(G.neighbors(node))
    return seen

The differences are:

    - I replaced the list called stack with a deque called queue.
    - I replaced pop with popleft, which removes and returns the leftmost element of the queue.

This version is back to being O(n + m). Now we’re ready to find shortest paths.