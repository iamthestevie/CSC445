import sys
from scipy.optimize import linprog


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
lp_content = []
print("Please put in your LP std input. To exit, please press 'q'.")
print("")
for line in sys.stdin:
    if 'q' == line.rstrip():
        print("You've exited from the input procedure.")
        break
    if '' == line.rstrip():
        print("Blank lines detected, please proceed with legal input or exit from the LP input procedure.")
        continue
    # print current input for debugging purposes
    print(f'Cur input : {line}')
    cur_line = [float(e) for e in line.split()]
    lp_content.append(cur_line)
# testing purpose
print(lp_content)



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

# Scipy implementation
# Scipy tries to find the minimum of the objective function
c = [-e for e in lp_content[0]]
A = [arr[:-1] for arr in lp_content[1:]]
b = [arr[-1] for arr in lp_content[1:]]
print(c)
print(A)
print(b)
res = linprog(c, A_ub = A, b_ub = b)




"""
################################################
### Section three: output                    ###
################################################
"""
status = res.status

# unbounded
if status == 2:
    print("Unbounded")
# infeasible
elif status == 3:
    print("Infeasible")
else:
    print('Optimal')
    print(res.x)





################################################
###      SIMPLEX ALGORITHM FROM SCRATCH      ###
################################################
SIMPLEX ALGORITHM FROM SCRATCH

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


    def pivot_position():
        """
        returns the pivot solution
        """


    def pivot_step(pivot_position):



    def can_be_improved():
        """
        Returns a boolean variable regarding whether it can be improved or not?
        """


    def solve():
        """
        Solves the linear program
        """

        # TODO: consider if it is initially feasible, if not, do more work

        # TODO: consider the unbounded scenario

        while self.can_be_improved():
            pivot_position = self.pivot_position()
            self.pivot_step(pivot_position)

        # TODO: return the result in your desired way, or store it in a class variable for users to retrieve. 







