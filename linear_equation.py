#import numpy as np
#
#
#A=np.mat('1,2; 4,5')
#Y=np.mat('3,6').T
#X=np.linalg.solve(A,Y)
#print(X)

from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

e1 = '4 * x - y - 3'
e2 = '2 * x + z - 7'
e3 = '3 * z - 2 * y - 8'

print(solve([e1, e2, e3],[x, y, z]))
