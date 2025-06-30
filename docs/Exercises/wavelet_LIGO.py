#!/usr/bin/env python

import math, copy, pywt
import numpy as np
import matplotlib.pyplot as mpl
from scipy import signal

def applyThreshold(val, threshold):
  return val if math.fabs(val) > threshold else 0.
applyThreshold = np.vectorize(applyThreshold, otypes=[np.float])

def filter(level):
  return 0.25*(1. + math.erf(level -2.)) * math.erfc(0.9*(level - 7))

def filterCoeffs(coeffs):
  filteredCoeffs = copy.deepcopy(coeffs)
  for level in range(1, len(coeffs)):
    rms = math.sqrt(np.mean(np.square(coeffs[level])))
    filteredCoeffs[level] = applyThreshold(coeffs[level], 1.3*rms)

  for level in range(0, len(coeffs)):
    filteredCoeffs[level] = filteredCoeffs[level] * filter(level)

  return filteredCoeffs

Hfile = open("H-H1_LOSC_4_V1-1126259446-32.txt", "rU")
LFile = open("L-L1_LOSC_4_V1-1126259446-32.txt", "rU")
HData = Hfile.readlines()
LData = LFile.readlines()

starttime=10
endtime=20

# this is the time difference between bins
dt = 1./4096.


HanfordTime=[]
LivingstonTime=[]
Hanford=[]
Livingston=[]

start=3
end=-1

time=0.
for line in HData[start:end]:
  line.strip("\n")
  Hanford.append(float(line))
  HanfordTime.append(time)
  time += dt

time=6.9/1000.
for line in LData[start:end]:
  line.strip("\n")
  Livingston.append(-float(line))
  LivingstonTime.append(time)
  time += dt

#mpl.plot(time, response)

mpl.plot(HanfordTime, Hanford, "r", LivingstonTime, Livingston, "b")
mpl.axis([starttime, endtime, -1e-18, 3e-18])
mpl.show()

# The widths array controls the sizes of the convolved wavelet function
widths = np.arange(10, 250., 10)

# Use scipy to do the transform
# the ricker function is a Mexican hat
# @todo can we replace that with another function from PyWavelets?
#cwt = signal.cwt(Hanford, signal.ricker, widths)

#mpl.imshow(cwt, extent=[0, len(Hanford)-1, 0., 250.], cmap='afmhot', aspect='auto', vmax=abs(cwt).max(), vmin=-abs(cwt).max())
#mpl.show()

# This is the wavelet basis
wb = pywt.Wavelet('sym4')

Hcoeffs = pywt.wavedec(Hanford, wb )
Lcoeffs = pywt.wavedec(Livingston, wb)

# Try filtering the coefficients to remove the high frequency jitter

# copy the original coefficients
filteredHCoeffs = filterCoeffs(Hcoeffs)
filteredLCoeffs = filterCoeffs(Lcoeffs)

filteredHanford = pywt.waverec(filteredHCoeffs, wb)
filteredLivingston = pywt.waverec(filteredLCoeffs, wb)


HanfordTime.append(HanfordTime[-1] + dt)
LivingstonTime.append(LivingstonTime[-1] + dt)


mpl.plot(HanfordTime,  filteredHanford, "r", LivingstonTime, filteredLivingston, "b")
mpl.axis([starttime, endtime, -1e-18, 1e-18])
mpl.show()




