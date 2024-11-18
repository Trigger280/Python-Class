import matplotlib as plt
import numpy as np

pi=3.14

start =1
end=3600
stepsize=10
X=np.arange(start,end,stepsize)

omega=10
omega2=30

Y=np.sin(2*pi*omega*X)
Y2=2*np.sin(2*pi*omega2*X)

plt.figure()
plt.plot(X,Y)
plt.plot(X,Y2)
