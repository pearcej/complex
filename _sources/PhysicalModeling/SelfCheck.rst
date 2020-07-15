Self Check
-------------

.. mchoice:: SC8_Q1
   :answer_a: True
   :answer_b: False
   :correct: a
   :feedback_a: Correct! When f=0.039 and k=0.065 the pattern that is produced looks like the patterns on animals. Though, this has not yet been proven.  
   :feedback_b: Incorrect, please refer back to section.

   There is a possibility for animal patterns to be based on diffusion reactions? 

.. dragndrop:: SC8_Q2  
   :match_1: 1|||Percolation models can be represented using cellular automatons. Below is an out of order representation of the processes of a 2-D CA that simulates percolation. Place them in the correct order  
   :match_2: 2|||Each cell is either “porous” with probability q or “non-porous” with probability 1-q 
   :match_3: 3|||When the simulation begins, all cells are considered “dry” except the top row, which is “wet”
   :match_4: 4|||During each time step, if a porous cell has at least one wet neighbor, it becomes wet. Non-porous cells stay dry
   :match_5: 5|||The simulation runs until it reaches a “fixed point” where no more cells change state
   :match_6: 6|||If there is a path of wet cells from the top to the bottom row, we say that the CA has a “percolating cluster”
    
   Percolation models can be represented using cellular automatons. Below is an out of order representation of the processes of a 2-D CA that simulates percolation. Place them in the correct order.

.. mchoice:: SC8_Q3
   :answer_a: Critical phenomena
   :answer_b: Phase change
   :answer_c: Random walk
   :answer_d: None of the above
   :correct: b
   :feedback_a: Incorrect, critical phenomena are a common set of behaviors that a wide variety of systems display when they are at or near a critical point. 
   :feedback_b: Correct!
   :feedback_c: Incorrect. Random walk is used to estimate the the critical value more precisely 
   :feedback_d: Incorrect. There is one right answer

   What is the the rapid change in behavior near the critical value called?

.. parsonsprob:: SC8_Q4
    :language: python

    Please put the test_perc function together so that it will run.  
    -----
    def test_perc(perc):
    =====
        num_wet = perc.num_wet()
    =====
        while True:
            perc.step()
    =====
            if perc.bottom_row_wet():
                return True
    =====
            new_num_wet = perc.num_wet()
    =====
            if new_num_wet == num_wet:
                return False
    =====
            num_wet = new_num_wet