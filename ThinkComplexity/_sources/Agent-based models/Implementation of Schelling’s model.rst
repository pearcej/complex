Implementation of Schelling’s model
-------------------------------------

To implement Schelling’s model, I wrote yet another class that inherits from ``Cell2D``:

::

    class Schelling(Cell2D):

        def __init__(self, n, p):
            self.p = p
            choices = [0, 1, 2]
            probs = [0.1, 0.45, 0.45]
            self.array = np.random.choice(choices, (n, n), p=probs)

``n`` is the size of the grid, and ``p`` is the threshold on the fraction of similar neighbors. For example, if ``p=0.3``, an agent will be unhappy if fewer than 30% of their neighbors are the same color.

``array`` is a NumPy array where each cell is 0 if empty, 1 if occupied by a red agent, and 2 if occupied by a blue agent. Initially 10% of the cells are empty, 45% red, and 45% blue.

The ``step`` function for Schelling’s model is substantially more complicated than previous examples. If you are not interested in the details, you can skip to the next section. But if you stick around, you might pick up some NumPy tips.

First, I make boolean arrays that indicate which cells are red, blue, and empty:

::

    a = self.array
            red = a==1
            blue = a==2
            empty = a==0

<<<<<<< HEAD
Then I use ``correlate2d`` to count, for each location, the number of neighboring cells that are red, blue, and non-empty. We saw ``correlate2d`` in `Section 7.7`_.
=======
Then I use ``correlate2d`` to count, for each location, the number of neighboring cells that are red, blue, and non-empty. We saw ``correlate2d`` in :ref:`Section 7.7 <7.7>`.
>>>>>>> 961d64d129fe8ad4bac657368baf72ac974f7856

::

    options = dict(mode='same', boundary='wrap')

        kernel = np.array([[1, 1, 1],
                        [1, 0, 1],
                        [1, 1, 1]], dtype=np.int8)

        num_red = correlate2d(red, kernel, **options)
        num_blue = correlate2d(blue, kernel, **options)
        num_neighbors = num_red + num_blue

``options`` is a dictionary that contains the options we pass to ``correlate2d``. With ``mode='same'``, the result is the same size as the input. With ``boundary='wrap'``, the top edge is wrapped to meet the bottom, and the left edge is wrapped to meet the right.

``kernel`` indicates that we want to consider the eight neighbors that surround each cell.

After computing ``num_red`` and ``num_blue``, we can compute the fraction of neighbors, for each location, that are red and blue.

::

    frac_red = num_red / num_neighbors
    frac_blue = num_blue / num_neighbors

Then, we can compute the fraction of neighbors, for each agent, that are the same color as the agent. I use ``np.where``, which is like an element-wise if expression. The first parameter is a condition that selects elements from the second or third parameter.

::

    frac_same = np.where(red, frac_red, frac_blue)
    frac_same[empty] = np.nan

In this case, wherever ``red`` is ``True``, ``frac_same`` gets the corresponding element of ``frac_red``. Where ``red`` is ``False``, ``frac_same`` gets the corresponding element of ``frac_blue``. Finally, where ``empty`` indicates that a cell is empty, ``frac_same`` is set to ``np.nan``, which is a special value that indicates “Not a Number”.

Now we can identify the locations of the unhappy agents:

::

    unhappy = frac_same < self.p
    unhappy_locs = locs_where(unhappy)

``locs_where`` is a wrapper function for ``np.nonzero``:

::

    def locs_where(condition):
        return list(zip(*np.nonzero(condition)))

``np.nonzero`` takes an array and returns the coordinates of all non-zero cells; the result is a tuple of arrays, one for each dimension. Then ``locs_where`` uses ``list`` and ``zip`` to convert this result to a list of coordinate pairs.

Similarly, ``empty_locs`` is an array that contains the coordinates of the empty cells:

::

    empty_locs = locs_where(empty)

Now we get to the core of the simulation. We loop through the unhappy agents and move them:

::

    num_empty = np.sum(empty)
        for source in unhappy_locs:
            i = np.random.randint(num_empty)
            dest = empty_locs[i]

            a[dest] = a[source]
            a[source] = 0
            empty_locs[i] = source

``i`` is the index of a random empty cell; ``dest`` is a tuple containing the coordinates of the empty cell.

In order to move an agent, we copy its value (1 or 2) from ``source`` to ``dest``, and then set the value of ``source`` to 0 (since it is now empty).

Finally, we replace the entry in ``empty_locs`` with ``source``, so the cell that just became empty can be chosen by the next agent.




