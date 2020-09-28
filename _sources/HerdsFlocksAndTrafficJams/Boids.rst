..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _HFT_4:

Boids
-----

In 1987 Craig Reynolds published “Flocks, herds and schools: A distributed behavioral model”, which describes an agent-based model of herd behavior.

Agents in this model are called “Boids”, which is both a contraction of “bird-oid” and an accented pronunciation of “bird” (although Boids are also used to model fish and herding land animals).

Each agent simulates three behaviors:

**Flock centering:**  Move toward the center of the flock.

**Collision avoidance:**  Avoid obstacles, including other Boids.

**Velocity matching:**  Align velocity (speed and direction) with neighboring Boids.

Boids make decisions based on local information only; each Boid only sees (or pays attention to) other Boids in its field of vision.

In the repository for this book, you will find ``Boids7.py``, which contains an implementation of Boids, based in part on the description in Gary William Flake’s book, *The Computational Beauty of Nature.*

The given implementation uses VPython, which is a library that provides 3-D graphics. VPython provides a vector object, which can be used to represent the position and velocity of Boids in three dimensions.

.. mchoice:: q_11.4.2
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: Sorry but Boids only make decisions based on local information because they only pay attention to local Boids.
   :feedback_b: Correct!

   Boids make decisions based off of local information most of the time but they occasionally make decisions by looking at non local information.
