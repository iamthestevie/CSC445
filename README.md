# CSC445 Programming Project

CSC 445 - Linear Programming at University of Victoria - Summer 2022
Programming Project - LP Solver
Steve Muir - V00347783

# Running the program

In order to run the python script please type the following command (where '$' is the command prompt):

$ python3 solver.py < <input_file_name.txt>

# Solver Architecture

## Simplex Implementation

Language Used: Python

Packages used: sys, numpy, math

For a detailed explanation of the program functionality please see the comments in the
code itself. 

The simplex algorithm implemented here matches that taught in CSC 445 prior to learning
the 'Revised Simplex Method' that employs primarily Linear Algebra to solve LP's. Here
I employ primarily the algebraic functionality taught in the course. 

One key difference is that here I build a 'Tableau' representing all the objective and
basic variables of the linear program. By building the program in this way we avoid having
to explicitly track variable indices, since the variable columns do not change. That is 
x_1 can always be found at index 0 of the tableau and the constant value can always be
found at index -1, where -1 represents the last index of the tableau.

Solving the Linear Program is handled in the way taught in class. First the LP is examined
for initial feasibility. If it is initially feasible, the LP is solved using algebraic 
Simplex Method. If the LP is not initially feasible, then we construct an auxiliary problem
using the variable Omega.

## Solving Initially-Infeasible Problems

I chose to use the Auxiliary method to solve the initialization problem in the case of
initially infeasible LPs. This is done by constructing a new objective function consisting
of all zero coefficients and -1 in the extra column added for the Omega variable. An 
additional column is added to the tableau for Omega as well. Then Omega is pivoted into
the basis in the usual way, by choosing the 'most negative' basic variable to leave the
basis. 

After Omega is in the basis, we can employ our previously built functionality for both
choosing pivot variables and performing pivot steps, until we are left with an auxiliary
tableau that is either optimal, with objective value equal to zero, or not, indicating
that the original LP is infeasible.
