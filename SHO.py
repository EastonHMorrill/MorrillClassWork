from scipy.optimize import curve_fit
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt 
import bisection

def SHM(t, A, omega, phi, d):
    return A*np.cos(omega*t + phi) + d

t, y = np.loadtxt("", unpack=True)
sig = np.zeros(len(y))
sig.fill(0.001)

A = (y.max() - y.min())/2.0

cs = CubicSpline(t, y)
pairs = bisection.find_sign_changes(cs, 0.1, t.min(), t.max())
zeros = bisection.bisect(cs, pairs, 1E-10)

T = 0

for i in range(1, len(zeros)):
    T += zeros[i] - zeros[i-1]
T = 2*T/(len(zeros) - 1)
print(T)

phi = np.arccos(y[0]/A)
omega = 2*np.pi/T
print(A, omega, phi)

theta_0 = [A, omega, phi, 0.0]
theta, cov = curve_fit(SHM, t, y, p0=theta_0, sigma=sig)
print(theta)
print(np.sqrt(np.diag(cov)))
cor = np.zeros_like(cov)

for i in range(0, len(theta)):
    for j in range(0, len(theta)):
        ``