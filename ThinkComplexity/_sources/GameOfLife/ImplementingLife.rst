Implementing Life
------------------

.. _7.7:

The exercises at the end of this chapter ask you to experiment with and modify the Game of Life, and implement other 2-D cellular automatons. This section explains my implementation of GoL, which you can use as a starting place for your experiments.

To represent the state of the cells, I use a NumPy array of 8-bit unsigned integers. As an example, the following line creates a 10 by 10 array initialized with random values of 0 and 1.

::

    a = np.random.randint(2, size=(10, 10), dtype=np.uint8)

There are a few ways we can compute the GoL rules. The simplest is to use ``for`` loops to iterate through the rows and columns of the array:

::

    b = np.zeros_like(a)
    rows, cols = a.shape
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            state = a[i, j]
            neighbors = a[i-1:i+2, j-1:j+2]
            k = np.sum(neighbors) - state
            if state:
                if k==2 or k==3:
                    b[i, j] = 1
            else:
                if k == 3:
                    b[i, j] = 1

Initially, ``b`` is an array of zeros with the same size as ``a``. Each time through the loop, ``state`` is the condition of the center cell and ``neighbors`` is the 3x3 neighborhood. ``k`` is the number of live neighbors (not including the center cell). The nested ``if`` statements evaluate the GoL rules and turn on cells in ``b`` accordingly.

This implementation is a straightforward translation of the rules, but it is verbose and slow. We can do better using cross-correlation, as we saw in :ref:`Section 6.11 <6.11>`. There, we used ``np.correlate`` to compute a 1-D correlation. Now, to perform 2-D correlation, we’ll use ``correlate2d`` from ``scipy.signal``, a SciPy module that provides functions related to signal processing:




::

    from scipy.signal import correlate2d

    kernel = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

    c = correlate2d(a, kernel, mode='same')

What we called a “window” in the context of 1-D correlation is called a “kernel” in the context of 2-D correlation, but the idea is the same: ``correlate2d`` multiplies the kernel and the array to select a neighborhood, then adds up the result. This kernel selects the 8 neighbors that surround the center cell.

``correlate2d`` applies the kernel to each location in the array. With ``mode='same'``, the result has the same size as ``a``.

Now we can use logical operators to compute the rules:

::

    b = (c==3) | (c==2) & a
    b = b.astype(np.uint8)

The first line computes a boolean array with ``True`` where there should be a live cell and ``False`` elsewhere. Then ``astype`` converts the boolean array to an array of integers.

This version is faster, and probably good enough, but we can simplify it slightly by modifying the kernel:

::


    kernel = np.array([[1, 1, 1],
                    [1,10, 1],
                    [1, 1, 1]])

    c = correlate2d(a, kernel, mode='same')
    b = (c==3) | (c==12) | (c==13)
    b = b.astype(np.uint8

This version of the kernel includes the center cell and gives it a weight of 10. If the center cell is 0, the result is between 0 and 8; if the center cell is 1, the result is between 10 and 18. Using this kernel, we can simplify the logical operations, selecting only cells with the values 3, 12, and 13.

That might not seem like a big improvement, but it allows one more simplification: with this kernel, we can use a table to look up cell values, as we did in :ref:`Section 6.12 <6.12>`.

::

    table = np.zeros(20, dtype=np.uint8)
    table[[3, 12, 13]] = 1
    c = correlate2d(a, kernel, mode='same')
    b = table[c]


``table`` has zeros everywhere except locations 3, 12, and 13. When we use ``c`` as an index into ``table``, NumPy performs element-wise lookup; that is, it takes each value from ``c``, looks it up in ``table``, and puts the result into ``b``.

This version is faster and more concise than the others; the only drawback is that it takes more explaining.

``Life.py``, which is included in the repository for this book, provides a ``Life`` class that encapsulates this implementation of the rules. If you run ``Life.py``, you should see an animation of a “puffer train”, which is a spaceship that leaves a trail of detritus in its wake.




