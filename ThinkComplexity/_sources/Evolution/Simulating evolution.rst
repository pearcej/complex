Simulating evolution
---------------------

I start with a simple model that demonstrates a basic form of evolution. According to the theory, the following features are sufficient to produce evolution:

- Replicators: We need a population of agents that can reproduce in some way. We’ll start with replicators that make perfect copies of themselves. Later we’ll add imperfect copying, that is, mutation.
- Variation: We need variability in the population, that is, differences between individuals.
- Differential survival or reproduction: The differences between individuals have to affect their ability to survive or reproduce.

To simulate these features, we’ll define a population of agents that represent individual organisms. Each agent has genetic information, called its **genotype**, which is the information that gets copied when the agent replicates. In our model1, a genotype is represented by a sequence of N binary digits (zeros and ones), where N is a parameter we choose.

To generate variation, we create a population with a variety of genotypes; later we will explore mechanisms that create or increase variation.

Finally, to generate differential survival and reproduction, we define a function that maps from each genotype to a **fitness**, where fitness is a quantity related to the ability of an agent to survive or reproduce.