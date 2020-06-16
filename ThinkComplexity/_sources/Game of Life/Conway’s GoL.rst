Conway’s GoL
------------
One of the first cellular automatons to be studied, and probably the most popular of all time, is a 2-D CA called “The Game of Life”, or GoL for short. It was developed by John H. Conway and popularized in 1970 in Martin Gardner’s column in *Scientific American*. See http://thinkcomplex.com/gol.

The cells in GoL are arranged in a 2-D **grid**, that is, an array of rows and columns. Usually the grid is considered to be infinite, but in practice it is often “wrapped”; that is, the right edge is connected to the left, and the top edge to the bottom.

Each cell in the grid has two states — live and dead — and 8 neighbors — north, south, east, west, and the four diagonals. This set of neighbors is sometimes called a “Moore neighborhood”.

Like the 1-D CAs in the previous chapters, GoL evolves over time according to rules, which are like simple laws of physics.

In GoL, the next state of each cell depends on its current state and its number of live neighbors. If a cell is alive, it stays alive if it has 2 or 3 neighbors, and dies otherwise. If a cell is dead, it stays dead unless it has exactly 3 neighbors.

This behavior is loosely analogous to real cell growth: cells that are isolated or overcrowded die; at moderate densities they flourish.

GoL is popular because:

    - There are simple initial conditions that yield surprisingly complex behavior.

    - There are many interesting stable patterns: some oscillate (with various periods) and some move like the spaceships in Wolfram’s Rule 110 CA.
    - And like Rule 110, GoL is Turing complete.

    - Another factor that generated interest was Conway’s conjecture — that there is no initial condition that yields unbounded growth in the number of live cells — and the $50 bounty he offered to anyone who could prove or disprove it.

    - Finally, the increasing availability of computers made it possible to automate the computation and display the results graphically.

    