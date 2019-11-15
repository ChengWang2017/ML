#import numpy as np
#
#
#A=np.mat('1,2; 4,5')
#Y=np.mat('3,6').T
#X=np.linalg.solve(A,Y)
#print(X)
from pylab import *
from sympy import *
import numpy as np
import matplotlib.pyplot as pt



x = Symbol('x')
#y = x**3 - 2*x**2 + 3*x + 4
y = x**2
dy = y.diff(x)
print(dy)


f = lambdify(x, y, 'numpy')
df = lambdify(x, dy, 'numpy')

v = np.arange(-3,6,0.1)
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x_ticks = np.arange(-3,6,0.5)
pt.xticks(x_ticks)
pt.plot(v,f(v))
pt.plot(v,df(v))
pt.show()


#print(solve([e1, e2, e3],[x, y, z]))
print(solve([y],[x]))
