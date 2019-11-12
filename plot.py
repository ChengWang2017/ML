from pylab import *

import numpy as np
import matplotlib.pyplot as pt

x = np.arange(-20,20,0.1)
y1 = np.sin(x) + x
#y1 = 2*x
y2 = x
#y3 = x/2
y3 = x - np.sin(x)

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

pt.plot(x,y1)
pt.plot(x,y2)
pt.plot(x,y3)
pt.xlim(-2,10)
pt.ylim(-2,10)
pt.show()
