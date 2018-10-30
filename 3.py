import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


f = 1
fs = 100


x = np.arange(2*fs+1)
measurements1 = [np.sin(2*np.pi*f*i/fs) for i in x]


noise = np.random.normal(0, 0.1, len(x))
measurements2 = measurements1 + noise


plt.figure(figsize=(10, 6))
sns.set_style(style="darkgrid")
plt.plot([i/100 for i in x], measurements1)
plt.plot([i/100 for i in x], measurements2)
plt.ylabel("Amplitude"), plt.xlabel("Time[s]")
plt.legend(['Measurements 1', 'Measurements 2'])
plt.show()
