Exercises
---------------
The code for this chapter is in the Jupyter notebook ``chap12.ipynb`` in the repository for this book. Open the notebook, read the code, and run the cells. You can use this notebook to work on the following exercises. My solutions are in ``chap12soln.ipynb``.

**Exercise 1:**  The simulations in this chapter depend on conditions and parameters I chose arbitrarily. As an exercise, I encourage you to explore other conditions to see what effect they have on the results. Here are some suggestions:

1. Vary the initial conditions: instead of starting with all defectors, see what happens if you start with all cooperators, all TFT, or random agents.
2. In ``Tournament.melee``, I shuffle the agents at the beginning of each time step, so each agent plays against two randomly-chosen agents. What happens if you don’t shuffle? In that case, each agent plays against the same neighbors repeatedly. That might make it easier for a minority strategy to invade a majority, by taking advantage of locality.
3. Since each agent only plays against two other agents, the outcome of each round is highly variable: an agent that would do well against most other agents might get unlucky during any given round, or the other way around. What happens if you increase the number of opponents each agent plays against during each round? Or what if an agent’s fitness at the end of each step is the average of its current score and its fitness at the end of the previous round?
4. The function I chose for ``prob_survival`` varies from 0.7 to 0.9, so the least fit agent, with p=0.7, lives for 3.33 time steps on average, and the most fit agent lives for 10 time steps. What happens if you make the degree of differential survival more or less “aggressive"?
5. I chose ``num_rounds``=6 so that each element of the genome has roughly the same impact on the outcome of a match. But that is substantially shorter than what Alexrod used in his tournaments. What happens if you increase ``num_rounds``? Note: if you explore the effect of this parameter, you might want to modify ``Niceness`` to measure the niceness of the last 4 elements of the genome, which will be under more selective pressure as ``num_rounds`` increases.
6. My implementation has differential survival but not differential reproduction. What happens if you add differential reproduction?

**Exercise 2:**  In my simulations, the population never converges to a state where a majority share the same, presumably optimal, genotype. There are two possible explanations for this outcome: one is that there is no optimal strategy, because whenever the population is dominated by a majority genotype, that condition creates an opportunity for a minority to invade; the other possibility is that the mutation rate is high enough to maintain a diversity of genotypes.

To distinguish between these explanations, try lowering the mutation rate to see what happens. Alternatively, start with a random population and run without mutation until only one genotype survives. Or run with mutation until the system reaches something like a steady state; then turn off mutation and run until there is only one surviving genotype. What are the characteristics of the genotypes that prevail in these conditions?

**Exercise 3:**  The agents in my experiment are “reactive” in the sense that their choice during each round depends only on what the opponent did during previous rounds. Explore strategies that also take into account the agent’s past choices. These strategies can distinguish an opponent who retaliates from an opponent who defects without provocation.

1
Here’s a recent report with references to previous experiments: Barreda-Tarrazona, Jaramillo-Gutiérrez, Pavan, and Sabater-Grande, “Individual Characteristics vs. Experience: An Experimental Study on Cooperation in Prisoner’s Dilemma", Frontiers in Psychology, 2017; 8: 596. http://thinkcomplex.com/pdexp.
2
For an excellent video summarizing what we have discussed so far, see http://thinkcomplex.com/pdvid1.
3
And that introduces a whole new topic in game theory, the free-rider problem (see http://thinkcomplex.com/rider)