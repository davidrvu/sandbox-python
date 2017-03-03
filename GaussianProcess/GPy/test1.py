# pip install gpy
import GPy
import numpy as np
from IPython.display import display


#################################################
## Gaussian process regression tutorial
#################################################
## 1-dimensional model

def main():
    X = np.random.uniform(-3.,3.,(20,1))
    Y = np.sin(X) + np.random.randn(20,1)*0.05 #Y include some noise.

    #The first step is to define the covariance kernel we want to use for the model.
    kernel = GPy.kern.RBF(input_dim=1, variance=1., lengthscale=1.)

    #The parameter input_dim stands for the dimension of the input space. 
    #The parameters variance and lengthscale are optional, and default to 1. 
    #Many other kernels are implemented, type GPy.kern.<tab> to see a list

    #The inputs required for building the model are the observations and the kernel:
    m = GPy.models.GPRegression(X,Y,kernel)

    display(m)
    print "m = "
    print m

    fig = m.plot()
    print "fig = "
    print fig
    GPy.plotting.show(fig, filename='basic_gp_regression_notebook')

if __name__ == "__main__":
    main()