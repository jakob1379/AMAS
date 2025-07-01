#!/usr/bin/env python

# this script plots a simple Gaussian and then calculates its continuous wavelet transform
# Q: what happens when you use smaller wavelet widths, and why?
# What features in the Gaussian are you seeing?
# (uncomment line 34 and comment line 33, you can also play with this param youself!)

import math, copy, pywt
import numpy as np
import matplotlib.pyplot as mpl
from scipy import signal
from scipy.special import erfinv

# A Gaussian function
def gaussian(val, mean=0., width=20.):
  return math.exp(-0.5*((val-mean)/width)**2)
gaussian = np.vectorize(gaussian, otypes=[np.float])

# Discrete wavelets typically require a number of points that is radix 2
# We therefore use 128 points in our curve
x = np.arange(-64.,64.,1)

# initially we generate a smooth Gaussian example
y=gaussian(x)

mpl.plot(x, y, 'b+')
mpl.show()

# We are now going to do the continuous wavelet transform of the Gaussian

# The widths array controls the sizes of the convolved wavelet function
# Use the smaller widths range that is commented one the line below to experiment
widths = np.arange(0.5, 30., 0.5)
#widths = np.arange(0.001, 1., 0.001)

# Use scipy to do the transform
# the ricker function is a Mexican hat
# @todo can we replace that with another function from PyWavelets?
cwt = signal.cwt(y, signal.ricker, widths)

# Plot the coefficients from the cwt.  Note that the larger-scale
# features of the input distribution are at small values on the y-axis,
# smaller-scale features are at large values on the y-axis

mpl.imshow(cwt, extent=[-80, 80, 0.05, 20.], cmap='afmhot', aspect='auto', vmax=abs(cwt).max(), vmin=-abs(cwt).max())
mpl.show()









