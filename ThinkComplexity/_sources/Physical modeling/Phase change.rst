Phase change
------------
Now let’s test whether a random array contains a percolating cluster:

::

    def test_perc(perc):
        num_wet = perc.num_wet()

        while True:
            perc.step()

            if perc.bottom_row_wet():
                return True

            new_num_wet = perc.num_wet()
            if new_num_wet == num_wet:
                return False

            num_wet = new_num_wet

``test_perc`` takes a ``Percolation`` object as a parameter. Each time through the loop, it advances the CA one time step. It checks the bottom row to see if any cells are wet; if so, it returns ``True``, to indicate that there is a percolating cluster.

During each time step, it also computes the number of wet cells and checks whether the number increased since the last step. If not, we have reached a fixed point without finding a percolating cluster, so ``test_perc`` returns ``False``.

To estimate the probability of a percolating cluster, we generate many random arrays and test them:

::

    def estimate_prob_percolating(n=100, q=0.5, iters=100):
        t = [test_perc(Percolation(n, q)) for i in range(iters)]
        return np.mean(t)

``estimate_prob_percolating`` makes 100 Percolation objects with the given values of ``n`` and ``q`` and calls ``test_perc`` to see how many of them have a percolating cluster. The return value is the fraction of those that have a percolating cluster.

When ``p=0.55``, the probability of a percolating cluster is near 0. At ``p=0.60``, it is about 70%, and at ``p=0.65`` it is near 1. This rapid transition suggests that there is a critical value of ``p`` near 0.6.

We can estimate the critical value more precisely using a **random walk**. Starting from an initial value of ``q``, we construct a Percolation object and check whether it has a percolating cluster. If so, ``q`` is probably too high, so we decrease it. If not, ``q`` is probably too low, so we increase it.

Here’s the code:

::

    def find_critical(n=100, q=0.6, iters=100):
        qs = [q]
        for i in range(iters):
            perc = Percolation(n, q)
            if test_perc(perc):
                q -= 0.005
            else:
                q += 0.005
            qs.append(q)
        return qs

The result is a list of values for ``q``. We can estimate the critical value, ``q_crit``, by computing the mean of this list. With ``n=100`` the mean of ``qs`` is about ``0.59``; this value does not seem to depend on ``n``.

The rapid change in behavior near the critical value is called a **phase change** by analogy with phase changes in physical systems, like the way water changes from liquid to solid at its freezing point.

A wide variety of systems display a common set of behaviors and characteristics when they are at or near a critical point. These behaviors are known collectively as **critical phenomena**. In the next section, we explore one of them: fractal geometry.