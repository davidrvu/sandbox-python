import numpy
import matplotlib.pyplot as plt

mean = 0
std = 1 
num_samples = 1000
samples_normal = numpy.random.normal(mean, std, size=num_samples)
samples_uniform = numpy.random.uniform(low=0.0, high=1.0, size=1000)


plt.plot(samples_normal)
plt.show()

plt.plot(samples_uniform)
plt.show()