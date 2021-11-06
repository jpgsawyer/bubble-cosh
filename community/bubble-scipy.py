# Author: John Sawyer
# Date: 6 November 2021
# No rights reserved.
# Here is a much cleaner version of solving this that uses SCI PY for the heavy
# Lifting of finding a and b. It also detects a non solution.

from scipy.optimize import minimize
from math import cosh

# The error function by comparing the solutions at y=R1 and x=0 and y=R2 and x=H
def err(X,R1,R2,H):
    a,b = X
    x0 = a*cosh(-b/a)
    x1 = a*cosh((H-b)/a)
    err = abs(x0-R1)+abs(x1-R2)
    return err

# Calls the minimize function then checks for an error and returns the solution
def findAB(R1,R2,H):
    x0 = R1,R2
    res = minimize(err,x0,method='nelder-mead',args=(R1,R2,H),
               options={'xatol': 1e-8, 'disp': False})
    e = err(res.x,R1,R2,H)
    if(e>1e-8):
       print ("no solution")
       print ("err = ", e)
       return None,None
    else:
       return res.x

# Main input. Could read a file or take command line args here but... :D
if(__name__=="__main__"):
    D = 1.068
    R = D/2.
    H = 0.6
    a,b = findAB(R,R,H)
    if(a):
        print ("a = %f, b = %f"%(a,b))
