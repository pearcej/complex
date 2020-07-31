.. _HFT_5:

The Boid Algorithm
----------------------
``Boids7.py`` defines two classes: ``Boid``, which implements the Boid behaviors, and ``World``, which contains a list of Boids and a “carrot” the Boids are attracted to.

The ``Boid`` class defines the following methods:

- ``center``: Finds other Boids within range and computes a vector toward their centroid.

- ``avoid``: Finds objects, including other Boids, within a given range, and computes a vector that points away from their centroid.

- ``align``: Finds other Boids within range and computes the average of their headings.

- ``love``: Computes a vector that points toward the carrot.

Here’s the implementation of ``center``:

::

    def center(self, boids, radius=1, angle=1):
            neighbors = self.get_neighbors(boids, radius, angle)
            vecs = [boid.pos for boid in neighbors]
            return self.vector_toward_center(vecs)

The parameters ``radius`` and ``angle`` are the radius and angle of the field of view, which determines which other Boids are taken into consideration. ``radius`` is in arbitrary units of length; ``angle`` is in radians.

``center`` USES ``get_neighbors`` to get a list of ``Boid`` objects that are in the field of view. ``vecs`` is a list of ``Vector`` objects that represent their positions.

Finally, ``vector_toward_center`` computes a ``Vector`` that points from ``self`` to the centroid of ``neighbors``.

Here’s how ``get_neighbors`` works:

::

    def get_neighbors(self, boids, radius, angle):
            neighbors = []
            for boid in boids:
                if boid is self:
                    continue

                # if not in range, skip it
                offset = boid.pos - self.pos
                if offset.mag > radius:
                    continue

                # if not within viewing angle, skip it
                if self.vel.diff_angle(offset) > angle:
                    continue

                # otherwise add it to the list
                neighbors.append(boid)

            return neighbors

For each other Boid, ``get_neighbors`` uses vector subtraction to compute the vector from ``self`` to ``boid``. The magnitude of this vector is the distance between them; if this magnitude exceeds ``radius``, we ignore ``boid``.

``diff_angle`` computes the angle between the velocity of ``self``, which points in the direction the Boid is heading, and the position of ``boid``. If this ``angle`` exceeds angle, we ignore ``boid``.

Otherwise boid is in view, so we add it to ``neighbors``.

Now here’s the implementation of ``vector_toward_center``, which computes a vector from ``self`` to the centroid of its neighbors.

::

    def vector_toward_center(self, vecs):
            if vecs:
                center = np.mean(vecs)
                toward = vector(center - self.pos)
                return limit_vector(toward)
            else:
                return null_vector

VPython vectors work with NumPy, so ``np.mean`` computes the mean of ``vecs``, which is a sequence of vectors. ``limit_vector`` limits the magnitude of the result to 1; ``null_vector`` has magnitude 0.

We use the same helper methods to implement ``avoid``:

::

    def avoid(self, boids, carrot, radius=0.3, angle=np.pi):
            objects = boids + [carrot]
            neighbors = self.get_neighbors(objects, radius, angle)
            vecs = [boid.pos for boid in neighbors]
            return -self.vector_toward_center(vecs)

``avoid`` is similar to ``center``, but it takes into account the carrot as well as the other Boids. Also, the parameters are different: ``radius`` is smaller, so Boids only avoid objects that are too close, and ``angle`` is wider, so Boids avoid objects from all directions. Finally, the result from ``vector_toward_center`` is negated, so it points *away* from the centroid of any objects that are too close.

Here’s the implementation of ``align``:

::

    def align(self, boids, radius=0.5, angle=1):
            neighbors = self.get_neighbors(boids, radius, angle)
            vecs = [boid.vel for boid in neighbors]
            return self.vector_toward_center(vecs)

``align`` is also similar to ``center``; the big difference is that it computes the average of the neighbors’ velocities, rather than their positions. If the neighbors point in a particular direction, the Boid tends to steer toward that direction.

Finally, ``love`` computes a vector that points in the direction of the carrot.

::

    def love(self, carrot):
            toward = carrot.pos - self.pos
            return limit_vector(toward)

The results from ``center``, ``avoid``, ``align``, and ``love`` are what Reynolds calls “acceleration requests", where each request is intended to achieve a different goal.

.. dragndrop:: q_11.5.1
    :match_1: Center|||Finds other Boids within range and computes a vector toward their centroid.
    :match_2: Avoid|||Finds objects, including other Boids, within a given range, and computes a vector that points away from their centroid.
    :match_3: Align|||Finds other Boids within range and computes the average of their headings.
    :match_4: Love|||Computes a vector that points toward the carrot.