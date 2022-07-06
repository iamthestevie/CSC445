import sys
import numpy as np
from scipy.optimize import linprog

###############################################
### Class: Linear Program ###
###############################################

class Linear_Program:
    def __init__(self, lp_content):
        """
        Function description:

        Input:
            A:
            B:
            C:
        -------------
        Output:
        """
        self.A = [arr[:-1] for arr in lp_content[1:]]
        self.b = [arr[-1] for arr in lp_content[1:]]
        self.c = [e for e in lp_content[0]]
        self.solution_state = 'optimal'

    # TODO: transform it in the tableu form
    def to_equation_tableu_form(self):    
        # append to a values for our slack variables
        for row in range(len(self.A)):
            self.c.append(0)
            for column in range(len(self.A)):
                if row == column:
                    self.A[row].append(1)
                else:
                    self.A[row].append(0)
        
        xb = [eq + [x] for eq, x in zip(self.A, self.b)]
        z = self.c + [0]
        self.lp_mat = xb + [z]
        print("#debugging print:", self.lp_mat)             



    def pivot_position(self):
        """
        returns the pivot solution
        """


        
    def pivot_step(self, pivot_position):



    def can_be_improved():
        """
        Returns a boolean variable regarding whether it can be improved or not?
        """
        for val in lp_mat[-1][:-1]:
            if val > 0:
                return True
        
        return False


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

if __name__ == '__main__':
    lp_content = []
    for line in sys.stdin:
        if 'q' == line.rstrip():
            print("You've exited from the input procedure.")
            break
        if '' == line.rstrip():
            print("Blank lines detected, please proceed with legal input or exit from the LP input procedure.")
            continue
        # print current input for debugging purposes
        cur_line = [float(e) for e in line.split()]
        lp_content.append(cur_line)


    lp = Linear_Program(lp_content)
    lp.to_equation_tableu_form()
    # lp.solve()

    # print(lp.solution_state)
    # print(lp.result)