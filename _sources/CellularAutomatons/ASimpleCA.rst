.. _6.1:

A Simple CA
-------------

Cellular automatons are governed by rules that determine how the state of the cells changes over time.

As a trivial example, consider a cellular automaton (CA) with a single cell. The state of the cell during time step :math:`i` is an integer, :math:`x_i`. As an initial condition, suppose :math:`x0 = 0`.

Now all we need is a rule. Arbitrarily, I’ll pick :math:`x_{i+1} = x_i + 1`, which says that during each time step, the state of the CA gets incremented by 1. So this CA performs a simple calculation: it counts.

But this CA is atypical; normally the number of possible states is finite. As an example, suppose a cell can only have one of two states, 0 or 1. For a 2-state CA, we could write a rule like :math:`x_{i+1} = (x_i + 1) \% 2`, where % is the remainder (or modulus) operator.

The behavior of this CA is simple: it blinks. That is, the state of the cell switches between 0 and 1 during each time step.

Most CAs are deterministic, which means that rules do not have any random elements; given the same initial state, they always produce the same result. But some CAs are nondeterministic; we will see examples later.

The CA in this section has only one cell, so we can think of it as zero-dimensional. In the rest of this chapter, we explore one-dimensional (1-D) CAs; in the next chapter we explore two-dimensional CAs.