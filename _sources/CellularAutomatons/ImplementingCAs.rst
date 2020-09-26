..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _CA_11:

Implementing CAs
----------------

To generate the figures in this chapter, I wrote a Python class called ``Cell1D`` that represents a 1-D cellular automaton, and a class called ``Cell1DViewer`` that plots the results. Both are defined in ``Cell1D.py`` in the repository for this book.

To store the state of the CA, I use a NumPy array with one column for each cell and one row for each time step.

To explain how my implementation works, I’ll start with a CA that computes the parity of the cells in each neighborhood. The “parity” of a number is 0 if the number is even and 1 if it is odd.

I use the NumPy function ``zeros`` to create an array of zeros, then put a 1 in the middle of the first row.

::

    rows = 5
    cols = 11
    array = np.zeros((rows, cols), dtype=np.uint8)
    array[0, 5] = 1
    print(array)

    [[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]

The data type ``uint8`` indicates that the elements of ``array`` are unsigned 8-bit integers.

``plot_ca`` displays the elements of an ``array`` graphically:

::

    import matplotlib.pyplot as plt

    def plot_ca(array, rows, cols):
        cmap = plt.get_cmap('Blues')
        plt.imshow(array, cmap=cmap, interpolation='none')

I import ``pyplot`` with the abbreviated name ``plt``, which is conventional. The function ``get_cmap`` returns a colormap, which maps from the values in the array to colors. The colormap ``'Blues'`` draws the “on" cells in dark blue and the “off" cells in light blue.

``imshow`` displays the array as an “image”; that is, it draws a colored square for each element of the array. Setting ``interpolation`` to ``none`` indicates that ``imshow`` should not interpolate between on and off cells.

To compute the state of the CA during time step ``i``, we have to add up consecutive elements of array and compute the parity of the sum. We can do that using a slice operator to select the elements and the modulus operator to compute parity:

::


    def step(array, i):
        rows, cols = array.shape
        row = array[i-1]
        for j in range(1, cols):
            elts = row[j-1:j+2]
            array[i, j] = sum(elts) % 2

``rows`` and ``cols`` are the dimensions of the array. ``row`` is the previous row of the array.

Each time through the loop, we select three elements from ``row``, add them up, compute the parity, and store the result in row ``i``.

In this example, the lattice is finite, so the first and last cells have only one neighbor. To handle this special case, I don’t update the first and last column; they are always 0.
