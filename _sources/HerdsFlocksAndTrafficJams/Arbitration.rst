..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _HFT_6:

Arbitration
-----------

To arbitrate among these possibly conflicting goals, we compute a weighted sum of the four requests:

::

    def set_goal(self, boids, carrot):
            w_avoid = 10
            w_center = 3
            w_align = 1
            w_love = 10

            self.goal = (w_center * self.center(boids) +
                        w_avoid * self.avoid(boids, carrot) +
                        w_align * self.align(boids) +
                        w_love * self.love(carrot))
            self.goal.mag = 1

``w_center``, ``w_avoid``, and the other weights determine the importance of the acceleration requests. Usually ``w_avoid`` is relatively high and ``w_align`` is relatively low.

After computing a goal for each Boid, we update their velocity and position:

::

    def move(self, mu=0.1, dt=0.1):
            self.vel = (1-mu) * self.vel + mu * self.goal
            self.vel.mag = 1
            self.pos += dt * self.vel
            self.axis = self.length * self.vel

The new velocity is the weighted sum of the old velocity and the goal. The parameter ``mu`` determines how quickly the birds can change speed and direction. Then we normalize velocity so its magnitude is 1, and orient the axis of the Boid to point in the direction it is moving.

To update position, we multiply velocity by the time step, ``dt``, to get the change in position. Finally, we update ``axis`` so the orientation of the Boid when it is drawn is aligned with its velocity.

Many parameters influence flock behavior, including the radius, angle and weight for each behavior, as well as maneuverability, ``mu``. These parameters determine the ability of the Boids to form and maintain a flock, and the patterns of motion and organization within the flock. For some settings, the Boids resemble a flock of birds; other settings resemble a school of fish or a cloud of flying insects.

As one of the exercises at the end of this chapter, you can modify these parameters and see how they affect Boid behavior.

.. fillintheblank:: CH11.6_Q1
    :casei:

    After computing a goal for each Boid, we update their |blank| and |blank|.

    - :velocity: Correct!
      :position: Nice try, but look at the ordering that it comes in the text
      :x: Incorrect, please try again.
    - :position: Correct!
      :velocity:  Nice try, but look at the ordering that it comes in the text
      :x: Incorrect, please try again.
