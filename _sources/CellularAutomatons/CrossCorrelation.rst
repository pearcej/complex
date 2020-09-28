..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _CA_12:

Cross-Correlation
-----------------

.. _6.11:

The operation in the previous section — selecting elements from an array and adding them up — is an example of an operation that is so useful, in so many domains, that it has a name: **cross-correlation**. And NumPy provides a function, called ``correlate``, that computes it. In this section we'll see how we can use NumPy to write a simpler, faster version of ``step``.

The NumPy ``correlate`` function takes an array, ``a``, and a “window", ``w``, with length N and computes a new array, ``c``, where element ``k`` is the following summation:

.. math::

   c_k = \sum_{n=0}^{N-1} a_{n+k}*W_n

We can write this operation in Python like this:

::

    def c_k(a, w, k):
        N = len(w)
        return sum(a[k:k+N] * w)

This function computes element ``k`` of the correlation between ``a`` and ``w``. To show how it works, we will create an array of integers:

::

    N = 10
    row = np.arange(N, dtype=np.uint8)
    print(row)

    [0 1 2 3 4 5 6 7 8 9]

And a window:

::

    window = [1, 1, 1]

    print(window)

With this window, each element, ``c_k``, is the sum of consecutive elements from ``a``:

::

    c_k(row, window, 0)
    3

    c_k(row, window, 1)
    6

We can use ``c_k`` to write ``correlate``, which computes the elements of ``c`` for all values of ``k`` where the window and the array overlap.

::

    def correlate(row, window):
        cols = len(row)
        N = len(window)
        c = [c_k(row, window, k) for k in range(cols-N+1)]
        return np.array(c)

Here’s the result:

::

    c = correlate(row, window)
    print(c)

    [ 3  6  9 12 15 18 21 24]

The NumPy function ``correlate`` does the same thing:

::

    c = np.correlate(row, window, mode='valid')
    print(c)

    [ 3  6  9 12 15 18 21 24]

The argument ``mode='valid'`` means that the result contains only the elements where the window and ``array`` overlap, which are considered valid.

The drawback of this mode is that the result is not the same size as ``array``. We can fix that with ``mode='same'``, which adds zeros to the beginning and end of ``array``:

::

    c = np.correlate(row, window, mode='same')
    print(c)

    [ 1  3  6  9 12 15 18 21 24 17]

Now the result is the same size as ``array``. As an exercise at the end of this chapter, you’ll have a chance to write a version of ``correlate`` that does the same thing.

We can use NumPy’s implementation of ``correlate`` to write a simple, faster version of ``step``:

::

    def step2(array, i, window=[1,1,1]):
    row = array[i-1]
    c = np.correlate(row, window, mode='same')
    array[i] = c % 2

In the notebook for this chapter, you’ll see that ``step2`` yields the same results as ``step``.
