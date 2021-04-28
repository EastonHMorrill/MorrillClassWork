import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x_i = []
y_i = []

def Langrange(x, x_i, y_i):
    N = len(x_i)
    result = 0
    for i in range(0, N):
        product = 1
        for j in range(0, N):
            if i != j:
                product = product*(x - x_i[j])/(x_i[i] - x_i[j])
        result = result + product*y_i[i]
    return result

x_i = [0, 3, 5, 7, 13]
y_i = [-7, 6, -1, 11, 18]

y_2 = Langrange(2, x_i, y_i)
y_9 = Langrange(9, x_i, y_i)

#print(y_2, y_9)

#------------------------------------------------------

def Gauss(x, mu, sigma):
    y = (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-(x - mu)**2/(2*sigma**2))
    return y

mu = 0
sigma = 1

x = np.linspace(-4, 4, 10)
y_l = Gauss(x, mu, sigma)

x_g = np.linspace(-4, 4, 1000)
y_g = Gauss(x_g, mu, sigma)

cs = CubicSpline(x, y_l)
print(cs(2), cs(9))

#print(y)

y = Langrange(x_g, x, y_l)
y_cs = cs(x_g)

plt.plot(x_g, y_g)
plt.plot(x_g, y)
plt.plot(x_g, y_cs)
plt.show()