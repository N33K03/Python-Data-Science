import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)  # linspace returns evenly spaced numbers over specified interval
y = np.sin(x)

plt.plot(x,y)
plt.show()