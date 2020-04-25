import numpy as np
import math


# finds the lower and upper bound on epsilon based on accuracy and budget constraints
def epsilon_bound(N, T, A, E, B):
    # accuracy constraint
    global e_lower
    e_lower = round((np.log(A - (2 * math.exp((-N * (T ** 2)) / 12)))) / (-(T * N) / 2), 7)

    # budget constraint
    global e_upper
    e_upper = round(np.log(1 + (B / (E * N))), 7)

    # checks the feasibility of N
    if e_lower > e_upper:
        return False
    else:
        return True


# inputs for all the variables
N = input('Initial N: ')
T = input('Desired Error: ')
A = input('Accuracy: ')
E = input('Base Cost: ')
B = input('Budget: ')
e_lower = None
e_upper = None

# increments N until its feasible
while True:
    while (A - (2 * math.exp((-N * (T ** 2)) / 12))) < 0:
        N = N + 1
    if epsilon_bound(N, T, A, E, B):
        break
    else:
        N = N + 1

Budget = ((math.exp(E))-1)*E*N

# printing results
print('\nFeasible N: ' + str(N) +
      '\nEpsilon Lower Bound: ' + str(e_lower) +
      '\nEpsilon Upper Bound: ' + str(e_upper) +
      '\nBudget: ' + str(Budget))
