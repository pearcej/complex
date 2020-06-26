Boids
--------
In 1987 Craig Reynolds published “Flocks, herds and schools: A distributed behavioral model”, which describes an agent-based model of herd behavior. You can download his paper from http://thinkcomplex.com/boid.

Agents in this model are called “Boids”, which is both a contraction of “bird-oid” and an accented pronunciation of “bird” (although Boids are also used to model fish and herding land animals).

Each agent simulates three behaviors:

**Flock centering:**  Move toward the center of the flock.

**Collision avoidance:**  Avoid obstacles, including other Boids.

**Velocity matching:**  Align velocity (speed and direction) with neighboring Boids.

Boids make decisions based on local information only; each Boid only sees (or pays attention to) other Boids in its field of vision.

In the repository for this book, you will find ``Boids7.py``, which contains my implementation of Boids, based in part on the description in Gary William Flake’s book, *The Computational Beauty of Nature.*

My implementation uses VPython, which is a library that provides 3-D graphics. VPython provides a Vector object, which I use to represent the position and velocity of Boids in three dimensions. You can read about them at http://thinkcomplex.com/vector.
