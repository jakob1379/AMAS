#!/usr/bin/env python

import math, copy, pywt
import numpy as np
import matplotlib.pyplot as mpl
from scipy import signal
from scipy.special import erfinv

# A Gaussian function
def gaussian(val, mean=0., width=20.):
  return math.exp(-0.5*((val-mean)/width)**2)
gaussian = np.vectorize(gaussian, otypes=[np.float])

# This function generates random noise that is normally distributed
# around a given signal shape with given statistics
# This uses the erf function, which is the cumulative distribution
# function of a Gaussian.  The inverse of the erf function can therefore
# be used to generate normally-distributed random numbers
np.random.seed(3032016)
def noise(signal, stats=1.):
  return math.sqrt(signal/stats)*erfinv(2.*np.random.rand()-1.)
noise = np.vectorize(noise, otypes=[np.float])

def applyThreshold(val, threshold):
  return val if math.fabs(val) > threshold else 0.
applyThreshold = np.vectorize(applyThreshold, otypes=[np.float])

# Discrete wavelets typically require a number of points that is radix 2
# We therefore use 128 points in our curve
x = np.arange(-64.,64.,1)

# initially we generate a smooth Gaussian example
y=gaussian(x)

# Then show a noisy version of the same Gaussian by adding a random
# component to each point,

# The value of "stats" determines the statistical power in the
# distribution - the higher stats, the smoother the curve and lower the
# noise

stats = 5.

noisyY = y + noise(y, stats)

mpl.plot(x, y, 'b+', x, noisyY, 'r')
mpl.show()

# We are now going to do the continuous wavelet transform of the clean
# and noisy signals.

# The widths array controls the sizes of the convolved wavelet function
widths = np.arange(0.5, 30., 0.5)

# Use scipy to do the transform
# the ricker function is a Mexican hat
# @todo can we replace that with another function from PyWavelets?
cwt = signal.cwt(y, signal.ricker, widths)

# Plot the coefficients from the cwt.  Note that the larger-scale
# features of the input distribution are at small values on the y-axis,
# smaller-scale features are at large values on the y-axis

mpl.imshow(cwt, extent=[-80, 80, 0.05, 20.], cmap='afmhot', aspect='auto', vmax=abs(cwt).max(), vmin=-abs(cwt).max())
mpl.show()

# now do the same to the noisy signal
cwt_noisy = signal.cwt(noisyY, signal.ricker, widths)

# note the separation between the noise and the original structure that
# was present in the original noiseless signal.  The noise appears as
# "fingers" at larger values on the y-axis
mpl.imshow(cwt_noisy, extent=[-80, 80, 0.05, 20.], cmap='afmhot', aspect='auto', vmax=abs(cwt_noisy).max(), vmin=-abs(cwt_noisy).max())
mpl.show()

# find the discrete wavelet coefficients of this noisy Gaussian
# This is a wavelet using the Daubechies D4 basis
d4 = pywt.Wavelet('db3')

# Apply it to the noisy Gaussian and get the wavelet coefficients
coeffs = pywt.wavedec(noisyY, d4, mode='per')

# Print out some info about the wavelet levels
for level in range(0,len(coeffs)):
  print "level " + str(level) + ": mean = " +str(np.mean(coeffs[level])) + ", RMS = " + str(math.sqrt(np.mean(np.square(coeffs[level]))))

print str(coeffs)


# Try filtering the coefficients to remove the high frequency jitter

# copy the original coefficients
filteredCoeffs = copy.deepcopy(coeffs)
# set all the coefficients at the last level (smallest size) to zero

for level in [-1, -2, -3]:

  filteredCoeffs[level] = np.zeros(len(filteredCoeffs[level]))

filteredY = pywt.waverec(filteredCoeffs, d4, mode='per')

mpl.plot(x, y, 'b+', x, noisyY, 'r', x, filteredY, 'g')
mpl.show()

# An alternative is to threshold the coefficients - set anything to zero
# that is less than the RMS for the level

# Can play around with this to get the best results
# @todo try soft thresholding, using variance instead of RMS as the threshold, other tricks...

thresholdedCoeffs = copy.deepcopy(coeffs)
for level in range(1, len(coeffs)):
  rms = math.sqrt(np.mean(np.square(coeffs[level])))
  thresholdedCoeffs[level] = applyThreshold(coeffs[level], rms)

for level in [-1, -2, -3]:
  thresholdedCoeffs[level] = np.zeros(len(thresholdedCoeffs[level]))

thresholdedY = pywt.waverec(thresholdedCoeffs, d4, mode='per')

mpl.plot(x, y, 'b+', x, noisyY, 'r', x, thresholdedY, 'g')
mpl.show()







