Simulating evolution
---------------------------

I start with a simple model that demonstrates a basic form of evolution. According to the theory, the following features are sufficient to produce evolution:

- **Replicators**: We need a population of agents that can reproduce in some way. We’ll start with replicators that make perfect copies of themselves. Later we’ll add imperfect copying, that is, mutation.
- **Variation**: We need variability in the population, that is, differences between individuals.
- **Differential survival** or **reproduction**: The differences between individuals have to affect their ability to survive or reproduce.

To simulate these features, we’ll define a population of agents that represent individual organisms. Each agent has genetic information, called its **genotype**, which is the information that gets copied when the agent replicates. In our model1, a genotype is represented by a sequence of ``N`` binary digits (zeros and ones), where ``N`` is a parameter we choose.

To generate variation, we create a population with a variety of genotypes; later we will explore mechanisms that create or increase variation.

Finally, to generate differential survival and reproduction, we define a function that maps from each genotype to a **fitness**, where fitness is a quantity related to the ability of an agent to survive or reproduce.

.. mchoice:: q_12.2
   :answer_a: Replicators
   :answer_b: Variations
   :answer_c: Fitness
   :answer_d: Differential survival or reproduction
   :answer_e: Genotype 
   :correct: a,b,d
   :feedback_a: Correct, they needed a population of agents that could reproduce in some way, and they used replicators that make perfect copies of themselves.
   :feedback_b: Correct, we need variability in the population, that is, differences between individuals.
   :feedback_c: Sorry this is a way to define one of the features.
   :feedback_d: Correct, the differences between individuals have to affect their ability to survive or reproduce.
   :feedback_e: This is what is needed to produce one of the three.

   Evolution needs three things to be present, what are those three things? 