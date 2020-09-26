..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _CA_7:

.. _CA_FIG_4:

Spaceships
----------

.. _fig_TC_reference:


.. figure:: Figures/thinkcomplexity2019.png
   :align: center
   :alt: "Figure 7.4: Rule 110 after 100 time steps."

   Figure 7.4: Rule 110 after 100 time steps.

.. _CA_FIG_5:

The behavior of Class 4 CAs is even more surprising. Several 1-D CAs, most notably Rule 110, are **Turing complete**, which means that they can compute any computable function. This property, also called **universality**, was proved by Matthew Cook in 1998.

:ref:`Figure 7.4 <CA_FIG_4>` shows what Rule 110 looks like with an initial condition of a single cell and 100 time steps. At this time scale it is not apparent that anything special is going on. There are some regular patterns but also some features that are hard to characterize.

:ref:`Figure 7.5<CA_FIG_5>` shows a bigger picture, starting with a random initial condition and 600 time steps:

.. figure:: Figures/thinkcomplexity2020.png
   :align: center
   :alt: "Figure 7.5: Rule 110 with random initial conditions and 600 time steps."

   Figure 7.5: Rule 110 with random initial conditions and 600 time steps.

After about 100 steps the background settles into a simple repeating pattern, but there are a number of persistent structures that appear as disturbances in the background. Some of these structures are stable, so they appear as vertical lines. Others translate in space, appearing as diagonals with different slopes, depending on how many time steps they take to shift by one column. These structures are called spaceships.

Collisions between spaceships yield different results depending on the types of the spaceships and the phase they are in when they collide. Some collisions annihilate both ships; others leave one ship unchanged; still others yield one or more ships of different types.

These collisions are the basis of computation in a Rule 110 CA. If you think of spaceships as signals that propagate through space, and collisions as gates that compute logical operations like AND and OR, you can see what it means for a CA to perform a computation.
