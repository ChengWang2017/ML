#from pylab import *
#
#import numpy as np
#import matplotlib.pyplot as pt
#
#x = np.arange(-20,20,0.1)
#y1 = np.sin(x) + x
##y1 = 2*x
#y2 = x
##y3 = x/2
#y3 = x - np.sin(x)
#
#ax = gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))
#
#pt.plot(x,y1)
#pt.plot(x,y2)
#pt.plot(x,y3)
#pt.xlim(-2,10)
#pt.ylim(-2,10)
#pt.show()

import numpy as np
import matplotlib.pyplot as plt
#a = 1
#t = np.linspace(0 , 2 * np.pi, 1024)
#X = a*(2*np.cos(t)-np.cos(2*t))
#Y = a*(2*np.sin(t)-np.sin(2*t))
#plt.plot(Y, X,color='r')
#plt.show()


x = np.linspace(-8 , 8, 1024)
y1 = 0.618*np.abs(x) - 0.8* np.sqrt(64-x**2)
y2 = 0.618*np.abs(x) + 0.8* np.sqrt(64-x**2)
plt.plot(x, y1, color = 'r')
plt.plot(x, y2, color = 'r')
plt.show()

