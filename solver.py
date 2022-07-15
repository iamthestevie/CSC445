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
        self.aux_solution_state = 'infeasible'
        self.lp_m = len(self.A)
        self.lp_n = len(self.c)


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
        # print("LINE 61: debugging print - lp_mat:", lp_mat)
        return lp_mat


    def pivot_position(self, lp_mat, aux=False):
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
        for eq in lp_mat[:-1]:
            coefficient = eq[entering_i]
            bounds.append(math.inf if coefficient <= 0 else eq[-1] / coefficient)

        if min(bounds) is math.inf:
            if aux == False:
                self.solution_state = "unbounded"
            else:
                self.aux_solution_state = "unbounded"

        leaving_i = bounds.index(min(bounds))
        
        #print("#LINE 93: debugging print: current pivot position is", leaving_i, entering_i)

        # return: 
        #           leaving_i  - the index of the basic variable to leave the basis.
        #           entering_i - the index of objective variable to enter the basis, 
        return leaving_i, entering_i
        

    def pivot_step(self, pivot_position, lp_mat):
        new_tableau = [[] for i in range(len(lp_mat))]
        
        i, j = pivot_position
        new_tableau[i] = np.array(lp_mat[i]) / lp_mat[i][j] # we want our exiting varaible to have coefficient of 1
        
        for row, eq in enumerate(lp_mat):
            if row != i:
                multiplier_row = np.array(new_tableau[i]) * lp_mat[row][j]
                new_tableau[row] = np.array(lp_mat[row]) - multiplier_row # matrix row manipulation
       
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

    def solve_auxiliary(self, lp_mat):
        """
        """
        # Step 1:   
        #   create a new aux tableau that will hold all the equations of our old
        #   tableu with one new varible for omega inserged right before the constant
        #   in the second to last index, and our new objective value
        
        auxiliary_tableau = [[] for i in range(len(lp_mat))]

        # Step 2:
        #   replace the objective function with objective value (minus) omega
        #   we can't discard the old objective function since we'll need it,
        #   however it is saved as part of the linear_program class as self.c
        #   we also need some attribute to track the state of the auxiliary objective value

        aux_objective_function = [0 for i in lp_mat[-1]]
        aux_objective_function.insert(-1, -1)
        auxiliary_tableau[-1] = aux_objective_function
        
        for row, eq in enumerate(lp_mat[:-1]):
            auxiliary_tableau[row] = eq
            auxiliary_tableau[row].insert(-1, -1)

        self.aux_solution_state == "infeasible"

        #print(f"LINE 166: debugging print - auxiliary_tableau: {auxiliary_tableau}")

        # Step 3:
        #   pivot omega into the basis
        #   need to create a new pivot_position function (or do we?) to do this since
        #   we no longer need to determine the variable to enter the basis.
        entering_i = len(auxiliary_tableau[-1]) - 2     # index of omega
        leaving_i = self.b.index(min(self.b))           # index of the 'most negative' basis variable
        pivot_position = (leaving_i, entering_i)

        omega_in_basis_tableau = self.pivot_step(pivot_position, auxiliary_tableau)

        # Step 4:
        #   we now have an initially feasible tableu.
        #   we can use the aux_pivot_step() function to check with the objective value can be optimized
        #   i.e. can it be made to be zero so that our original LP has an initially feasible point
        #   that we can then use to solve it.

        while self.can_be_improved(omega_in_basis_tableau) and self.aux_solution_state == "infeasible":
                pivot_position = self.pivot_position(omega_in_basis_tableau, True)
                if self.aux_solution_state != "infeasible":
                    break
                omega_in_basis_tableau = self.pivot_step(pivot_position, omega_in_basis_tableau)
        
        # Step 5:
        #   if the objective value is zero we can convert our aux tableu back to its original
        #   LP with the basis of the auxiliary tableu.
        #   otherwise if the objective value is not zero then the original LP is infeasible
        # for eq in omega_in_basis_tableau:
        #     print(eq)

        if omega_in_basis_tableau[-1][-1] != 0: # or self.aux_solution_state == "unbounded"
            return False, False
        else:
            return 0, omega_in_basis_tableau


    def convert_aux_original(self, auxiliary_tableau):

        # Step 1:
        #   remove omega
        for row in range(len(auxiliary_tableau)):
            auxiliary_tableau[row] = np.delete(auxiliary_tableau[row], -2)

        auxiliary_tableau = np.array(auxiliary_tableau)
        
        # Step 2:
        #   iterate through the coefficients of the objective function
        #   up to the constant column since we do not need to include the constant value
        # for var_i in range(len(auxiliary_tableau[-1])-1):
        for var_i in range(self.lp_n):
 
            # find out what is the difference in coefficients
            # original: 5x1 + 3x2
            # currently: 2x1
            # difference for coeff_x1 = 5-2 = 3
        
            dif_aux_original = self.c[var_i] - auxiliary_tableau[-1][var_i]
            for row in auxiliary_tableau[:-1]:
                if row[var_i] != 0:
                    multiplier = dif_aux_original / row[var_i]
                    new_row = - np.array(row)
                    new_row[-1] = - new_row[-1]
                    new_row[var_i] = 0
                    auxiliary_tableau[-1] += multiplier * new_row
                    break

        auxiliary_tableau[-1][-1] *= -1            
        return auxiliary_tableau


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
        #   sum(n < 0 for n in nums)
        if not self.can_be_improved(lp_tableu) or sum(n < 0 for n in self.b) > 0:
            # then solve the auxiliary form
            auxiliary_solution, auxiliary_tableau = self.solve_auxiliary(lp_tableu)

            # check if it is feasible
            if auxiliary_solution == 0:
                self.solution_state == 'optimal'
                lp_tableu = self.convert_aux_original(auxiliary_tableau)
                #print("lp returned from convert_aux: ", lp_tableu)

                while self.can_be_improved(lp_tableu) and self.solution_state == "optimal":
                    pivot_position = self.pivot_position(lp_tableu)
                    if self.solution_state != "optimal":
                        break
                    lp_tableu = self.pivot_step(pivot_position, lp_tableu)
                    
                    # for row in lp_tableu:
                    #     print(row)


                self.obj_value = lp_tableu[-1][-1]
                self.get_solution(lp_tableu)

            else:
                self.solution_state = 'infeasible'

        else:
            while self.can_be_improved(lp_tableu) and self.solution_state == "optimal":

                # for row in lp_tableu:
                #         print(row)

                pivot_position = self.pivot_position(lp_tableu)
                if self.solution_state != "optimal":
                    break
                lp_tableu = self.pivot_step(pivot_position, lp_tableu)

            self.obj_value = lp_tableu[-1][-1]
            self.get_solution(lp_tableu)

    
    def display_result(self):
        print(self.solution_state)
        if self.solution_state == 'optimal':
            print(self.obj_value)
            print(self.result)

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
    lp.display_result()