##############################
# D. Jason Koskinen
# Mar. 25, 2016
#
#
# This uses dust logger data from 
# core sample(s) in Antarctica
# and is problem set 2 question 3
#
# Data is from http://nsidc.org/data/NSIDC-0540/versions/1/metadata
# http://nsidc.org/data/docs/agdc/nsidc0540/index.html
##############################

import matplotlib
matplotlib.use('Agg')


import io, os, sys
import json
import math
import numpy
import pymultinest
import scipy
from scipy import interpolate, stats


from ROOT import TCanvas, TF1, TH1F, TGraph, TLegend, TStyle, TH2D, TGraphErrors, TH2F
from ROOT import gStyle
from array import array

savePlots = True

# The prior sets the range
# for the variables

def prior(cube, ndim, nparams):
    for i in range(ndim):
        cube[i] = cube[i] * 8 * math.pi
    # end for
# end def prior

def loglike(cube, ndim, nparams, lnew):
        chi = 1.
        for i in range(ndim):
            chi *= math.cos(cube[i] / 2.)
        # end for
        return math.pow(2. + chi, 5)
# end def

# number of dimensions our problem has
parameters = ["position x", "position y"]
n_params = len(parameters)
print '\n n_params: ', n_params


#run MultiNest
pymultinest.run(loglike, prior, n_params, outputfiles_basename='out/d-',
	resume = False, verbose = True,
    n_live_points = 300, max_iter = 1500)

a = pymultinest.Analyzer( n_params = n_params, outputfiles_basename='out/d-')
s = a.get_stats()
posterior = a.get_equal_weighted_posterior()

##############################
# Draw the underlying LLH landscape
##############################
scale_w = 8*math.pi
h2Egg = TH2F("h2", "Egg Carton Likelihood Landscape;#theta_{1};#theta_{2}", 100, 0, scale_w, 100, 0, scale_w)
for i in numpy.arange(0.001, scale_w, scale_w/100):
    for j in numpy.arange(0.001, scale_w, scale_w/100):
        h2Egg.Fill(i, j, loglike([i,j], 2, 2, 2))
    # end for j
# end for i

tCan0 = TCanvas()
h2Egg.Draw("COLZ")
h2Egg.SetStats(0)
tCan0.Update()
    
if savePlots:
    tCan0.SaveAs("EggCartonLikelihood.pdf")
# end


##############################
# Draw the posterior
##############################

grPosterior_1 = TGraph( len(posterior), numpy.array(posterior[:,0]), numpy.array(posterior[:,1]))

tCanPosterior_0 = TCanvas()
grPosterior_1.SetTitle("Egg Carton Posterior (MultiNest)")
grPosterior_1.Draw("AP*")
grPosterior_1.GetXaxis().SetTitle("#theta_{1}")
grPosterior_1.GetYaxis().SetTitle("#theta_{2}")
tCanPosterior_0.Update()

if savePlots:
    tCanPosterior_0.SaveAs("EggCartonPosterior.pdf")
# end

######################################################################
# Do another example
######################################################################
base_dir_name = "out/circ-"

r = 2.
w = 0.1

const = math.log(1. / math.sqrt(2. * math.pi * w**2))
print "const,",  const

def logcirc(theta, c, r):
    d = numpy.sqrt((theta[0]-c[0])**2 + (theta[1]-c[1])**2)
    return const - (d - r)**2 / (2. * w**2)

def circPrior(cube, ndim, nparams):
    for i in range(ndim):
        cube[i] = cube[i] * 6
    # end for
# end def

def circLoglike(cube, ndim, nparams):
    theta = numpy.array( [cube[0], cube[1]])
    c1 = numpy.array([2.5, 3.1])
    c2 = numpy.array([2.7, 2.7])
    #return numpy.exp(logcirc(theta, c1, 2)) + 1.5*numpy.exp(logcirc(theta, c2, 1)) + 0.001
    return numpy.exp(logcirc(theta, c1,r))+0.0001
# end def circLoglike

parameters = ["x", "y"]
n_params = len(parameters)

pymultinest.run(circLoglike, circPrior, n_params, outputfiles_basename=base_dir_name,
	resume = False, verbose = True,
    n_live_points = 300, max_iter = 15000
    )

a_circ = pymultinest.Analyzer( n_params = n_params, outputfiles_basename=base_dir_name)
posterior_circ = a_circ.get_equal_weighted_posterior()

grPosterior_2 = TGraph( len(posterior_circ), numpy.array(posterior_circ[:,0]), numpy.array(posterior_circ[:,1]))

range_w = 6.
h2Circ = TH2F("h2Circ", "Gaussian Shell Landscape;#theta_{1};#theta_{2}", 100, 0, range_w, 100, 0, range_w)
for i in numpy.arange( 0.001, range_w, range_w/100):
    for j in numpy.arange( 0.001, range_w, range_w/100):
        h2Circ.Fill(i, j, circLoglike([i,j], 2, 1))
    # end for j
# end for i

tCanGaussShell = TCanvas("canGauss", "", 450, 450)
h2Circ.Draw("COLZ")
h2Circ.SetStats(0)
#h2Circ.Draw("LEGO2Z")
grPosterior_2.SetMarkerStyle(6)
grPosterior_2.Draw("P")
tCanGaussShell.Update()

if savePlots:
    tCanGaussShell.SaveAs("GaussShell_LH.pdf")
# end if

raw_input('Press Enter to exit')

######################################################################
# for the ev.dat data files
#
## This file contains the set of rejected points. It has nPar+3 
## columns. The first nPar columns are the ndim
## parameter values along with the (nPar-ndim)  additional 
## parameters that are being passed by the likelihood
## routine for MultiNest to save along with the ndim parameters. 
## The nPar+1 column is the log-likelihood value,
## nPar+2 column is the log(prior mass) & the last column  is the 
## node no. (used for clustering).


# for the get_data() function
## [root].txt
## Compatable with getdist with 2+nPar columns. Columns have 
## sample probability, -2*loglikehood, samples. Sample
## probability is the sample prior mass multiplied by its 
## likelihood & normalized by the evidence.
## """    

