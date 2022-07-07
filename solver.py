import sys
import numpy as np
import math

###############################################
### Class: Linear Program ###
###############################################

class Linear_Program:
    def __init__(self, lp_content):
        """
        Function description:

        Input: lp_content:
            A:
            b:
            c:
        -------------
        Output:
        """
        self.A = [arr[:-1] for arr in lp_content[1:]]
        self.b = [arr[-1] for arr in lp_content[1:]]
        self.c = [e for e in lp_content[0]]
        self.solution_state = 'optimal'


    def to_equation_tableu_form(self):
        """
        Function Description:
        Adds all the slack variables so that the function 
        is in the required equation form...
        
        z  + (c1)x1   ... (cn)xn (0)w1     ... (0)wm
        b1 - (a1,1)x1 ... (a1,n)xn - (1)w1 ... (0)wm
        .
        .
        .
        bm - (am,1)x1 ... (am,n)xn (0)w1 ... (1)wm

        Input: self

        Ouput: None

        """
        
        # append to a values for our slack variables
        equation_count = len(self.A)
        for row in range(equation_count):
            for column in range(equation_count):
                if row == column:
                    self.A[row].append(1)
                else:
                    self.A[row].append(0)
            self.c.append(0)

        
        xb = [eq + [x] for eq, x in zip(self.A, self.b)]
        z = self.c + [0]
        self.lp_mat = xb + [z]
        print("#debugging print:", self.lp_mat)             



    def pivot_position(self):
        """
        returns the pivot position
        """
        # STEP 1: find the non basic variable that we want to work on
        obj_fun = self.lp_mat[-1]#
        for var_i in range(len(obj_fun[:-1])):
            if obj_fun[var_i] > 0:
                break

        # STEP 2: find the most strict boundary for var_i th non basic variable
        # thought process: 
            # go through all the euqations (rows of the matrix) row by row
                # calculate and then store the constraint
            # find the smallest constraint and return the var_i, and the row of the constraint (pivot position)

        # return var_i, row of the tightest constraint
        
    def pivot_step(self, pivot_position):
        """
        
        """
        # TODO: construct a new tableau of all the entries updated with the entering variable
        # tip:
            # Think about the below example that we talked about in class.
            # say that we will be wiping out x2, then the coefficient of x1 will be 1.5 + 4 * 1.5
            # x1    x2    x3   x4   x5    x6      b
            # 1.5     4     1     0    0     0   =  4   
            # 4     2     0     1    0     0   =  5
       
        self.lp_mat = new_tableau



    def can_be_improved(self):
        """
        Returns a boolean variable regarding whether it can be improved or not?
        """
        for num in self.lp_mat[-1][:-1]:
            if num > 0:
                return True
        return False


    def is_initially_feasible(self):
        for eq in self.lp_mat[:-1]:
            if eq[-1] < 0:
                return False
        return True

    
    def solve(self):
        """
        """
        self.to_equation_tableu_form()
        # TODO: think about the while loop we talked about in class
        # TODO: consider different edge cases, like infeasible/unbounaded/

        #self.result = # TODO: feel free to change this part depending on your implementation
        #self.solution_state # TODO: feel free to change this part depending on your implementation


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
        if '' == line.rstrip():
            continue
        # print current input for debugging purposes
        cur_line = [float(e) for e in line.split()]
        lp_content.append(cur_line)

    lp = Linear_Program(lp_content)
    lp.to_equation_tableu_form()
    # lp.solve()
    # print(lp.solution_state)
    # print(lp.result)