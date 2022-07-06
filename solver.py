import sys
import numpy as np
from scipy.optimize import linprog

###############################################
### Class: Linear Program ###
###############################################

class Linear_Program:
    def __init__(self, A, b, c):
        """
        Function description:

        Input:
            A:
            B:
            C:
        -------------
        Output:
        """
        self.A = A
        self.b = b
        self.c = c

        # TODO: transform it in the tableu form


    def pivot_position(self):
        """
        returns the pivot solution
        """

        
    def pivot_step(self, pivot_position):



    # def can_be_improved():
        """
        Returns a boolean variable regarding whether it can be improved or not?
        """

        # Is the dictionary initially feasible?

    def is_initially_feasible(self):
        for val in self.b > 0:
            print(val)


    def solve(self):
        """
        Solves the linear program
        """

        # TODO: consider if it is initially feasible, if not, do more work

        # TODO: consider the unbounded scenario
        self.is_initially_feasible()

        # while self.can_be_improved():
        #     pivot_position = self.pivot_position()
        #     self.pivot_step(pivot_position)

        # TODO: return the result in your desired way, or store it in a class variable for users to retrieve. 


###############################################
### Section one: Read in the standard input ###
###############################################
"""
TODOS:
   - What are cases we should check?
   - How do we save?
   - How do we let the user start and exit from the program?
   - Maybe these user prompts/instructions shouldn't be added considering the grading schema 
     (if the only thing auto grader wants is to print is the result).
"""

lp_content = []                                     # list to hold data

for line in sys.stdin:
    if '' == line.rstrip():                         # skip blank lines
        continue
    # print(f'Cur input : {line}')                    # print current input for debugging purposes
    cur_line = [float(e) for e in line.split()]     # split line and cast values into float type
    lp_content.append(cur_line)                     # append values to our list

# print(lp_content)



################################################
### Section two: Solve ###
################################################
"""
In Python, there are different libraries for linear programming:
   - the multi-purposed SciPy
      https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

   - the beginner-friendly PuLP
   https://towardsdatascience.com/how-to-create-your-first-linear-programming-solver-in-python-284e3fe5b811
   
   - the exhaustive Pyomo
"""

c = [e for e in lp_content[0]]                     # coefficients of the objective function
A = [arr[:-1] for arr in lp_content[1:]]           # constraints
b = [arr[-1] for arr in lp_content[1:]]            # constants

print(f'Objective function: {c}')
print(f'Constraints: {A}')
print(f'Constants: {b}')


np_c = np.array(c)
np_A = np.array(A)
np_b = np.array(b)

lp = Linear_Program(np_A, np_b, np_c)
lp.solve()



"""
################################################
### Section three: output                    ###
################################################
"""



################################################
###      SIMPLEX ALGORITHM FROM SCRATCH      ###
################################################

"""
Pseudo code in class exercise:
def solve():
    while can_be_improved():
        choose varible to enter the basis
        inspect bounds
        choose the variable to leave the basis
        perform pivot

    output results
"""



"""
Start with a class called linear program that takes in the input we got,
saves it in a reasonable format, and solves it using simplex. 
More functions may need to be added. 
Think about independence and abstraction between different functions. 
After the linear program class is completed, this replaces what we did in step two in the above program. 
"""











