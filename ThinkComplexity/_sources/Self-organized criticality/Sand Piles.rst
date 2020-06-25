Sand Piles
----------
The sand pile model was proposed by Bak, Tang and Wiesenfeld in 1987. It is not meant to be a realistic model of a sand pile, but rather an abstraction that models physical systems with a large number of elements that interact with their neighbors.

The sand pile model is a 2-D cellular automaton where the state of each cell represents the slope of a part of a sand pile. During each time step, each cell is checked to see whether it exceeds a critical value, *K*, which is usually 3. If so, it “topples” and transfers sand to four neighboring cells; that is, the slope of the cell is decreased by 4, and each of the neighbors is increased by 1. At the perimeter of the grid, all cells are kept at slope 0, so the excess spills over the edge.

Bak, Tang and Wiesenfeld initialize all cells at a level greater than K and run the model until it stabilizes. Then they observe the effect of small perturbations: they choose a cell at random, increment its value by 1, and run the model again until it stabilizes.

For each perturbation, they measure ``T``, the number of time steps the pile takes to stabilize, and ``S``, the total number of cells that topple.

Most of the time, dropping a single grain causes no cells to topple, so ``T=1`` and ``S=0``. But occasionally a single grain can cause an **avalanche** that affects a substantial fraction of the grid. The distributions of ``T`` and ``S`` turn out to be heavy-tailed, which supports the claim that the system is in a critical state.

They conclude that the sand pile model exhibits “self-organized criticality”, which means that it evolves toward a critical state without the need for external control or what they call “fine tuning” of any parameters. And the model stays in a critical state as more grains are added.

In the next few sections I replicate their experiments and interpret the results.

.. fillintheblank:: q_9.3
   :casei:

   Bak, Tang and Wiesenfeld conclude that the sand pile model exhibits |blank|, which means that it evolves toward a |blank| without the need for |blank|.

   - :self organized criticality: Correct!
     :x: Incorrect, please reread the section.
   - :critical state: Correct!
     :x: Incorrect, please reread the section.    
   - :external control: Correct!
     :x: Incorrect, please reread the section.
     