import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Håvard Kråkenes - 26.10.2018
Simulates 10 seconds of pendulum d^2theta/d^2t + c*sin(theta) = 0
theta0 = pi/2
omega0 = 0
'''


def dtheta(omega):
    return omega


def domega(theta):
    return -4.9*np.sin(theta)


dt = 0.001
t = 10
n = int(t/dt)


def RK4(dtheta, du, theta0, omega0, n, dt):
    omega = [omega0]
    theta = [theta0]

    for t in range(n-1):
        # Calculate next theta value
        kt1 = dtheta(omega[t])
        kt2 = dtheta(omega[t] + 0.5 * dt * kt1)
        kt3 = dtheta(omega[t] + 0.5 * dt * kt2)
        kt4 = dtheta(omega[t] + dt * kt3)
        thetanext = theta[t] + (dt/6) * (kt1 + 2*kt2 + 2*kt3 + kt4)

        # Calculate next omega value
        ku1 = du(theta[t])
        ku2 = du(theta[t] + 0.5 * dt * ku1)
        ku3 = du(theta[t] + 0.5 * dt * ku2)
        ku4 = du(theta[t] + dt * ku3)
        omeganext = omega[t] + (dt/6) * (ku1 + 2*ku2 + 2*ku3 + ku4)

        omega.append(omeganext)
        theta.append(thetanext)

    return omega, theta


omega, theta = RK4(dtheta, domega, np.pi/2, 0, n, dt)


# Plot theta vs time
plt.figure(figsize=(10, 6))
sns.set_style(style="darkgrid")
plt.plot(np.linspace(0, 10, int(t/dt)), [i/np.pi*180 for i in theta])
plt.ylabel("Degrees"), plt.xlabel("time[s]")
plt.show()
