from scipy.integrate import fixed_quad
from scipy.interpolate import CubicSpline
import numpy as np

def func(x):
    return (x-2)**3 - 3.5*x + 8.0

def deriv(x):
    return 3*(x-2)**2 - 3.5

def int(a, b):
    upper = ((1/2)*b**2)*(1/4)*(b-2)**4 - (3.5/2)*b**2 + 8.0*b
    lower = ((1/2)*a**2)*(1/4)*(a-2)**4 - (3.5/2)*a**2 + 8.0*a
    return upper, lower

def CentralDiff(f, x, h):
    return (f(x+h/2) - f(x-h/2))/h

print(int(0.0, 4.0))

x = np.linspace(0.0, 4.0, 5)
y = func(x)

cs = CubicSpline(x, y)
result, err = fixed_quad(cs, 0.0, 4.0, n=2)
print(result)

result, err = fixed_quad(func, 0.0, 4.0, n=2)
print(result)

