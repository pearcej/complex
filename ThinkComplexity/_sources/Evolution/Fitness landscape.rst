Fitness landscape
------------------

The function that maps from genotype to fitness is called a **fitness landscape**. In the landscape metaphor, each genotype corresponds to a location in an N-dimensional space, and fitness corresponds to the “height" of the landscape at that location. For visualizations that might clarify this metaphor, see http://thinkcomplex.com/fit.

In biological terms, the fitness landscape represents information about how the genotype of an organism is related to its physical form and capabilities, called its **phenotype**, and how the phenotype interacts with its **environment**.

In the real world, fitness landscapes are complicated, but we don’t need to build a realistic model. To induce evolution, we need *some* relationship between genotype and fitness, but it turns out that it can be *any* relationship. To demonstrate this point, we’ll use a totally random fitness landscape.

Here is the definition for a class that represents a fitness landscape:

::

    class FitnessLandscape:

        def __init__(self, N):
            self.N = N
            self.one_values = np.random.random(N)
            self.zero_values = np.random.random(N)

        def fitness(self, loc):
            fs = np.where(loc, self.one_values,
                            self.zero_values)
            return fs.mean()

The genotype of an agent, which corresponds to its location in the fitness landscape, is represented by a NumPy array of zeros and ones called loc. The fitness of a given genotype is the mean of N **fitness contributions**, one for each element of loc.

To compute the fitness of a genotype, FitnessLandscape uses two arrays: one_values, which contains the fitness contributions of having a 1 in each element of loc, and zero_values, which contains the fitness contributions of having a 0.

The fitness method uses np.where to select a value from one_values where loc has a 1, and a value from zero_values where loc has a 0.

As an example, suppose N=3 and

::

    one_values =  [0.1, 0.2, 0.3]
    zero_values = [0.4, 0.7, 0.9]

In that case, the fitness of loc = [0, 1, 0] would be the mean of [0.4, 0.2, 0.9], which is 0.5.


