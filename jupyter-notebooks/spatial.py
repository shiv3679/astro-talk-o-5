# importing the libraries

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# N = 1000 -- number of stars in the system
# generating the random sample of masses

X_1 = np.random.uniform(0,1,size=10000)

# finding the radius shell for the corresponding masses given by the function r(m)

radius = 1/np.sqrt(X_1**(-2/3) - 1)
radius

# generating theta and phi as random numbers 

theta = np.random.uniform(0,1,size=10000)
phi = np.random.uniform(0,1,size=10000)

z = (1-2*theta)*radius
x = (radius**2 - z**2)**(1/2)*np.cos(2*np.pi*phi)
y = (radius**2 + z**2)**(1/2)*np.sin(2*np.pi*phi)

fig = plt.figure()

ax = plt.axes(projection = '3d')

ax.plot3D(0,0,0,'gd')
ax.plot3D(x,y,z,'ro')
plt.title('Plummer halo system (spatial subspace)')
plt.legend(['center of the halo (0,0,0)','stars in the system'])
plt.show()