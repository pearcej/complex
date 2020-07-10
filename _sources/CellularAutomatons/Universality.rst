Universality
------------



To understand universality, we have to understand computability theory, which is about models of computation and what they compute.

One of the most general models of computation is the Turing machine, which is an abstract computer proposed by Alan Turing in 1936. A Turing machine is a 1-D CA, infinite in both directions, augmented with a read-write head. At any time, the head is positioned over a single cell. It can read the state of that cell (usually there are only two states) and it can write a new value into the cell.

In addition, the machine has a register, which records the state of the machine (one of a finite number of states), and a table of rules. For each machine state and cell state, the table specifies an action. Actions include modifying the cell the head is over and moving one cell to the left or right.

A Turing machine is not a practical design for a computer, but it models common computer architectures. For a given program running on a real computer, it is possible (at least in principle) to construct a Turing machine that performs an equivalent computation.

The Turing machine is useful because it is possible to characterize the set of functions that can be computed by a Turing machine, which is what Turing did. Functions in this set are called “Turing computable".

To say that a Turing machine can compute any Turing-computable function is a tautology: it is true by definition. But Turing-computability is more interesting than that.

It turns out that just about every reasonable model of computation anyone has come up with is “Turing complete"; that is, it can compute exactly the same set of functions as the Turing machine. Some of these models, like lamdba calculus, are very different from a Turing machine, so their equivalence is surprising.

This observation led to the **Church-Turing Thesis**, which is the claim that these definitions of computability capture something essential that is independent of any particular model of computation.

The Rule 110 CA is yet another model of computation, and remarkable for its simplicity. That it, too, turns out to be Turing complete lends support to the Church-Turing Thesis.

In *A New Kind of Science*, Wolfram states a variation of this thesis, which he calls the “principle of computational equivalence” (see http://thinkcomplex.com/equiv):

Almost all processes that are not obviously simple can be viewed as computations of equivalent sophistication.
More specifically, the principle of computational equivalence says that systems found in the natural world can perform computations up to a maximal (“universal”) level of computational power, and that most systems do in fact attain this maximal level of computational power. Consequently, most systems are computationally equivalent.

Applying these definitions to CAs, Classes 1 and 2 are “obviously simple”. It may be less obvious that Class 3 is simple, but in a way perfect randomness is as simple as perfect order; complexity happens in between. So Wolfram’s claim is that Class 4 behavior is common in the natural world, and that almost all systems that manifest it are computationally equivalent.

.. mchoice:: q1_6.8
    :answer_a: True
    :answer_b:  False
    :correct: a
    :feedback_a: Correct!
    :feedback_b: Incorrect.

    The Turing machine is useful because it is possible to characterize the set of functions that can be computed by it. 