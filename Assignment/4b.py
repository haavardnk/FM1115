import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Time unit: 1 h
beta = 10/(40*8*24)
gamma = 3/(15*24)
dt = 5  # 5 hours
# dt = 20 # 20 hours
D = 30  # Simulate for D days
N_t = int(D*24/dt)  # Corresponding no of hours

t = np.linspace(0, N_t*dt, N_t+1)

S_fe = np.zeros(N_t+1)
I_fe = np.zeros(N_t+1)
R_fe = np.zeros(N_t+1)

S_he = np.zeros(N_t+1)
I_he = np.zeros(N_t+1)
R_he = np.zeros(N_t+1)

# Initial condition
S_fe[0] = 50
I_fe[0] = 1
R_fe[0] = 0

S_he[0] = 50
I_he[0] = 1
R_he[0] = 0

# Step equations forward in time
for n in range(N_t):
    # FE
    S_fe[n+1] = S_fe[n]-dt*beta*S_fe[n]*I_fe[n]
    I_fe[n+1] = I_fe[n]+dt*beta*S_fe[n]*I_fe[n]-dt*gamma*I_fe[n]
    R_fe[n+1] = R_fe[n]+dt*gamma*I_fe[n]
    # HE*
    S_dot = S_he[n]-dt*beta*S_he[n]*I_he[n]
    I_dot = I_he[n]+dt*beta*S_he[n]*I_he[n]-dt*gamma*I_he[n]
    R_dot = R_he[n]+dt*gamma*I_he[n]
    # HE
    S_he[n+1] = S_he[n]-(dt/2)*(beta*S_he[n]*I_he[n]+beta*S_dot*I_dot)
    I_he[n+1] = I_he[n]+(dt/2)*((beta*S_he[n]*I_he[n] -
                                 gamma*I_he[n])+(beta*S_dot*I_dot-gamma*I_dot))
    R_he[n+1] = R_he[n]+(dt/2)*(gamma*I_he[n]+gamma*I_dot)

plt.figure(figsize=(10, 6))
sns.set_style(style="darkgrid")
plt.plot(t, S_fe, marker='o', markevery=500)
plt.plot(t, I_fe, marker='v', markevery=500)
plt.plot(t, R_fe, marker='s', markevery=500)
plt.plot(t, S_he, marker='^', markevery=500)
plt.plot(t, I_he, marker='x', markevery=500)
plt.plot(t, R_he, marker='|', markevery=500)
plt.legend(['S_FE', 'I_FE', 'R_FE', 'S_HE', 'I_HE', 'R_HE'])
plt.xlabel('hours')
plt.show()
