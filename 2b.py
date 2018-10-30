import numpy as np
'''
Håvard Kråkenes - 23.10.2018
Computes the answer of theta for d^2theta/d^2t + c*cos(theta) = 0
theta0 = pi/2
'''


def f(theta):
    return -4.9*np.cos(theta)


def dfdt(theta):
    return -4.9*(-np.sin(theta))


def Newton(f, dfdt, theta, eps):
    f_value = f(theta)
    iter_counter = 0
    while abs(f_value) > eps and iter_counter < 100:
        theta = theta - f_value/dfdt(theta)
        f_value = f(theta)
        iter_counter += 1
    return theta, iter_counter


solution, no_iter = Newton(f, dfdt, theta=(3*np.pi/4), eps=1.0E-10)

if no_iter > 0:  # Solution found
    print(f"Number of iterations of Newtons Method: {no_iter}")
    print(f"A solution is: {solution}")
else:
    print("Solution not found!")
