import numpy as np
import matplotlib.pyplot as plt


data= np.loadtxt('../Data/active_fraction_average.txt').T

#plot data
data_reduced= np.mean(data, axis= 1)/2500
plt.errorbar(np.arange(0.55, 0.705, 0.005), data_reduced, ecolor= 'k')
plt.title('Infection fraction average vs Infection probability')
plt.xlabel('Infection probabiolity, p$_1$')
plt.ylabel(r'Mean of infection fraction, $\frac{<I>}{N}$')
plt.savefig('../Plots/wave_mean.pdf')
plt.show()