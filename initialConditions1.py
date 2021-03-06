import numpy as np

# Initial conditions function for diffusion

def squareWave(x,alpha,beta):
    "A square wave as a function of position, x, which is 1 between alpha"
    "and beta and zero elsewhere. The initialisation is conservative so"
    "that each phi contains the correct quantity integrated over a region"
    "a distance dx/2 either side of x"
    
    phi = np.zeros_like(x)
    

    # Set phi away from the end points (assume zero at the end points)
    for j in xrange(1,len(x)-1):
        # edges of the grid box (using west and east notation)
        if x[j] > 0.4 and x[j] < 0.6:
            phi[j] = 1.0
        else:
            phi[j] = 0.0

    return phi


