import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


omega = 2
P = 2*np.pi/omega
dt = P/2000
T = 3*P
N_t = int(round(T/dt))
t = np.linspace(0, N_t*dt, N_t+1)


u = np.zeros(N_t+1)
v = np.zeros(N_t+1)


# Initial condition
X_0 = 2
u[0] = X_0
v[0] = 0


for n in range(1, N_t+1):
    u[n] = 1/(1+(dt*omega)**2) * (dt*v[n-1] + u[n-1])
    v[n] = 1/(1+(dt*omega)**2) * (v[n-1] - dt*omega**2*u[n-1])


plt.figure(figsize=(10, 6))
sns.set_style(style="darkgrid")
plt.plot(t, u, 'b-', t, X_0*np.cos(omega*t), 'r--')
plt.legend(['Numerical', 'Exact'])
plt.xlabel("Time[s]")
plt.show()
