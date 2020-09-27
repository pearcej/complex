..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _SFN_FIG_1:

Degree
------

.. _SFN_4:

.. figure:: Figures/thinkcomplexity2010.png
   :align: center
   :alt: "Figure 6.1: PMF of degree in the Facebook dataset and in the WS model."

   Figure 6.1: PMF of degree in the Facebook dataset and in the WS model.

If the WS graph is a good model for the Facebook network, it should have the same average degree across nodes, and ideally the same variance in degree.

This function returns a list of degrees in a graph, one for each node:

::

    def degrees(G):
        return [G.degree(u) for u in G]

The mean degree in model is :math:`44`, which is close to the mean degree in the dataset, :math:`43.7`.

However, the standard deviation of degree in the model is :math:`1.5`, which is not close to the standard deviation in the dataset, :math:`52.4`. Oops.

What’s the problem? To get a better view, we have to look at the distribution of degrees, not just the mean and standard deviation.

I’ll represent the distribution of degrees with a ``Pmf`` object, which is defined in the thinkstats2 module. ``Pmf`` stands for “probability mass function”.

Briefly, a ``Pmf`` maps from values to their probabilities. A ``Pmf`` of degrees is a mapping from each possible degree, ``d``, to the fraction of nodes with degree ``d``.

As an example, I’ll construct a graph with nodes :math:`1`, :math:`2`, and :math:`3` connected to a central node, :math:`0`:

::

    G = nx.Graph()
    G.add_edge(1, 0)
    G.add_edge(2, 0)
    G.add_edge(3, 0)
    nx.draw(G)

Here’s the list of degrees in this graph:

::

    >>> degrees(G)
    [3, 1, 1, 1]

Node :math:`0` has degree :math:`3`, the others have degree :math:`1`. Now I can make a ``Pmf`` that represents this degree distribution:

::

    >>> from thinkstats2 import Pmf
    >>> Pmf(degrees(G))
    Pmf({1: 0.75, 3: 0.25})

The result is a ``Pmf`` object that maps from each degree to a fraction or probability. In this example, :math:`75%` of the nodes have degree :math:`1` and :math:`25%` have degree :math:`3`.

Now we can make a ``Pmf`` that contains node degrees from the dataset, and compute the mean and standard deviation:

::

    >>> from thinkstats2 import Pmf
    >>> pmf_fb = Pmf(degrees(fb))
    >>> pmf_fb.Mean(), pmf_fb.Std()
    (43.691, 52.414)

And the same for the WS model:

::

    >>> pmf_ws = Pmf(degrees(ws))
    >>> pmf_ws.mean(), pmf_ws.std()
    (44.000, 1.465)

We can use the ``thinkplot`` module to plot the results:

::

    thinkplot.Pdf(pmf_fb, label='Facebook')
    thinkplot.Pdf(pmf_ws, label='WS graph')

:ref:`Figure 6.1<SFN_FIG_1>` shows the two distributions. They are very different.

In the WS model, most users have about :math:`44` friends; the minimum is :math:`38` and the maximum is :math:`50`. That’s not much variation. In the dataset, there are many users with only :math:`1` or :math:`2` friends, but one has more than :math:`1000`!

Distributions like this, with many small values and a few very large values, are called heavy-tailed.
