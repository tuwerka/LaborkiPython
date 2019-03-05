from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt

t = arange(0., 20., 2)

plt.plot(t, t, 'y--', t, t**2, 'cs', t, t**3, 'm^')
plt.title('Wonderful chart')
#plt.ylabel("")
plt.show()


x = linspace(-10., 10., 200)
y = 5*sin(x)-8**2
plt.plot(x, y, 'r-', label='theory')
plt.show()