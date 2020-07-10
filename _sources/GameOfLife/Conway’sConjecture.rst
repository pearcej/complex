.. _7.4:

Conway’s Conjecture
--------------------

From most initial conditions, GoL quickly reaches a stable state where the number of live cells is nearly constant (possibly with some oscillation).

.. figure:: Figures/figure_7.4.png
    :align: center
    :alt: "Figure 7.4: Starting and final configurations of the r-pentomino."

    Figure 7.4: Starting and final configurations of the r-pentomino.

.. _7.5:

But there are some simple starting conditions that yield a surprising number of live cells, and take a long time to settle down. Because these patterns are so long-lived, they are called “Methuselahs”.

One of the simplest Methuselahs is the r-pentomino, which has only five cells, roughly in the shape of the letter “r”. :ref:`Figure 7.4 <7.4>` shows the initial configuration of the r-pentomino and the final configuration after 1103 steps.

This configuration is “final” in the sense that all remaining patterns are either stable, oscillators, or gliders that will never collide with another pattern. In total, the r-pentomino yields 6 gliders, 8 blocks, 4 blinkers, 4 beehives, 1 boat, 1 ship, and 1 loaf.

.. figure:: Figures/figure_7.5.png
    :align: center
    :alt: "Figure 7.5: Gosper’s glider gun, which produces a stream of gliders."

    Figure 7.5: Gosper’s glider gun, which produces a stream of gliders.


The existence of long-lived patterns prompted Conway to wonder if there are initial patterns that never stabilize. He conjectured that there were not, but he described two kinds of pattern that would prove him wrong, a “gun” and a “puffer train”. A gun is a stable pattern that periodically produces a spaceship — as the stream of spaceships moves out from the source, the number of live cells grows indefinitely. A puffer train is a translating pattern that leaves live cells in its wake.

It turns out that both of these patterns exist. A team led by Bill Gosper discovered the first, a glider gun now called Gosper’s Gun, which is shown in :ref:`Figure 7.5 <7.5>`. Gosper also discovered the first puffer train.

There are many patterns of both types, but they are not easy to design or find. That is not a coincidence. Conway chose the rules of GoL so that his conjecture would not be obviously true or false. Of all possible rules for a 2-D CA, most yield simple behavior: most initial conditions stabilize quickly or grow unboundedly. By avoiding uninteresting CAs, Conway was also avoiding Wolfram’s Class 1 and Class 2 behavior, and probably Class 3 as well.

If we believe Wolfram’s Principle of Computational Equivalence, we expect GoL to be in Class 4, and it is. The Game of Life was proved Turing complete in 1982 (and again, independently, in 1983). Since then, several people have constructed GoL patterns that implement a Turing machine or another machine known to be Turing complete.

.. fillintheblank:: q_7.6
   :casei:

   Conway conjectured that there were no initial patterns that never stabilized. He described two kinds of patterns that would prove him wrong |blank| and |blank|.

   - :gun: Correct, it is a stable pattern that periodically produces a spaceship.
     :glider: No, sorry glider is proven to be a stable patern that settles. 
     :toad: Sorry, but toad is proven to be a stable pattern that settles. 
     :beehives: No, beehive is proven to be a stable pattern that settles.
     :r-pentomino: Incorrect, r-pintomino is proven to be a stable pattern that settles.
     :x: Incorrect, Please refer to Conway’s conjecture in the book.
   - :puffer train: Correct, it is a translating pattern that leaves live cells in its wake.
     :glider: No, sorry glider is proven to be a stable patern that settles.
     :toad: Sorry, this pattern is proven to be a stable pattern that settles.
     :beehives: No, beehive is proven to be a stable pattern that settles.
     :r-pentomino: Incorrect, r-pintomino is proven to be a stable pattern that settles.
     :x: Incorrect, Please refer to Conway’s conjecture in the book.

.. mchoice:: q_7.7
   :answer_a: It is a Methuselahs
   :answer_b: It is a beehive 
   :answer_c: It only has five cells
   :answer_d: It was one of the two patterns that Conway said would never stabilize and prove him wrong
   :answer_e: None of the above are true
   :correct: a,c
   :feedback_a: Correct! It has a simple starting condition and is long-lived.
   :feedback_b: Sorry a beehive is a stable pattern with each cell having two to three neighbors , so they all survive, and none of the dead cells adjacent to the beehive has 3 neighbors, so no new cells are born.
   :feedback_c: Correct!
   :feedback_d: Sorry the two patterns that Conway said could prove him wrong were actually a “gun” and a “puffer train”.
   :feedback_e: Sorry but two of the answers given above are correct. 

   
   Which of the following is true about r-pentomino? Select all that apply.

.. mchoice:: q_7.8
   :answer_a: True
   :answer_b: False
   :correct: a
   :feedback_a: Correct, Gosper's gun is the same gun that Conway said would prove him wrong.
   :feedback_b: Incorrect

   There was a prediction of Gosper's gun, a stable pattern that periodically produces a spaceship. As the stream of spaceships move out from the source, the number of live cells grows indefinitely.