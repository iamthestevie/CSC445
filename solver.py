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
        bm - (am,1)x1 ... (am,n)xn - (0)w1 ... (1)wm

        Input: self

        Ouput: None

        """

        # append to A values for our slack variables
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
        lp_mat = xb + [z]
        print("LINE 60: debugging print - lp_mat:", lp_mat)
        return lp_mat


    def pivot_position(self, lp_mat):
        """
        returns the pivot position
        """
        # STEP 1: find the non basic variable that we want to work on
        obj_fun = lp_mat[-1]
        for entering_i in range(len(obj_fun[:-1])):
            if obj_fun[entering_i] > 0:
                break

        # STEP 2: find the most strict boundary for entering_i the non basic variable
        # thought process: 
            # go through all the equations (rows of the matrix) row by row
                # calculate and then store the constraint
            # find the smallest constraint and return the entering_i, and the row of the constraint (pivot position)
        bounds = []
        for basis_eq in self.lp_mat[:-1]:
            coefficient = eq[entering_i]
            bounds.append(math.inf if coefficient <= 0 else eq[-1] / coefficient)

        if min(bounds) is math.inf:
            self.solution_state = "unbounded"

        leaving_i = restrictions.index(min(restrictions))
        
        print("#debugging print: current pivot position is", leaving_i, entering_i)

        # return: 
        #           leaving_i  - the index of the basic variable to leave the basis.
        #           entering_i - the index of objective variable to enter the basis, 
        return leaving_i, entering_i
        

    def pivot_step(self, pivot_position, lp_mat):
        new_tableau = [[] for i in range(len(self.lp_mat))]
        
        i, j = pivot_position
        new_tableau[i] = np.array(self.lp_mat[i]) / self.lp_mat[i][j] # we want our exiting varaible to have coefficient of 1
        
        for row, eq in enumerate(self.lp_mat):
            if row != i:
                multiplier_row = np.array(new_tableau[i]) * self.lp_mat[row][j]
                new_tableau[row] = np.array(self.lp_mat[row]) - multiplier_row # matrix row manipulation
       
        return new_tableau

    def is_pivot(self, column):
        return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) -1

    def get_solution(self, lp_mat):
        lp_mat_columns = np.array(lp_mat).T

        self.result = []
        for column in lp_mat_columns[:-1]:
            solution = 0
            if self.is_pivot(column):
                one_index = column.tolist().index(1)
                solution = lp_mat_columns[-1][one_index]
            self.result.append(solution)


    def can_be_improved(self, lp_mat):
        """
        Returns a boolean variable regarding whether it can be improved or not?
        """
        for num in lp_mat[-1][:-1]:
            if num > 0:
                return True
        return False


    def solve(self):
        """
        Solves the linear program in the following procedure:
        1. to equation tableu form
        2. TODO: consider if it is initially feasible, if not, do more work
        3. TODO: consider the unbounded scenario
        """
        lp_tableu = self.to_equation_tableu_form()
   
        # check objective function
        #   if it has no positive coefficients or,
        #   it has negative basic variables
        if not self.can_be_improved(lp_tableu) or any(self.b) < 0:
            # then solve the auxiliary form
            auxiliary_solution = self.solve_auxiliary(lp_tableu)




        # check if it is feasible
        if auxiliary_solution == 0:
            lp_tableu = self.to_equation_tableu_form()

            while self.can_be_improved(lp_tableu) and self.solution_state == "optimal":
                pivot_position = self.pivot_position(lp_tableu)
                if self.solution_state != "optimal":
                    break
                lp_tableu = self.pivot_step(pivot_position, lp_tableu)

            self.result = lp_tableu[-1][-1]
            self.get_solution(lp_tableu)

        else:
            self.solution_state = 'infeasible'


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
        if '' == line.rstrip(): # skip blank lines
            continue
        # print current input for debugging purposes
        cur_line = [float(e) for e in line.split()]
        lp_content.append(cur_line)

    lp = Linear_Program(lp_content)
    lp.solve()

    # print(lp.solution_state)
    # if lp.solution_state == 'optimal':
    #     print(lp.result)
    #     print(lp.solution)