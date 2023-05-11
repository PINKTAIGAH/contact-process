'''
Plot the variance of the infection fraction for varying p_i probability allong with resampled
errors
'''
import matplotlib.pyplot as plt
import numpy as np

def generate_resampled_var(data, n=1000):
    # Generate a resampled data set for Infection fraction and return it's variance
    resampled_dataset= np.random.choice(data, size=n)
    var= resampled_dataset.var()/2500
    return var

def find_resampled_variance(data, k=1000):
    # Return the errors from the resampled datasets
    variance_errors= []
    #Iterate over all p1 probabilities
    for i in range(data.shape[0]):
        bootstrapped_var= []
        for j in range(k):
            bootstrapped_var.append(generate_resampled_var(data[i][:]))
        variance_errors.append(np.array(bootstrapped_var).std())    
    return variance_errors

data= np.loadtxt('../Data/active_fraction_average.txt').T
errors= find_resampled_variance(data)
print(errors)

#plot data
data_reduced= np.var(data, axis= 1)/2500
plt.errorbar(np.arange(0.55, 0.705, 0.005), data_reduced, yerr= errors, ecolor= 'k')
plt.title('Infection fraction varience vs Infection probability')
plt.xlabel('Infection probabiolity, p$_1$')
plt.ylabel(r'Variance of infection fraction, $\frac{<I^2>-<I>^2}{N}$')
plt.savefig('../Plots/wave_variance.png')
plt.show()