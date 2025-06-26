#!/usr/local/bin/python3

import healpy as H
import sys
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import scipy.special as sp
import subprocess
import pickle
from scipy.optimize import fminbound
from scipy.optimize import minimize
import pyfits
from scipy.interpolate import interp1d
from scipy.special import erf
#from yt.mods import *

if __name__ == "__main__":
	
	rc('text', usetex=True)
	rc('font',**{'family':'serif','serif':['Palatino']})
	
	#f = open('LH_09_0_10000.dat', 'w',1)
	
	RUNS = 100000
	
	KS1 = np.array(pickle.load(open('C1iso_Ntot100_Nsample100000.dat', "br" )))
	KS2 = np.array(pickle.load(open('C1dipole_Ntot100_Nsample100000.dat', "br" )))
	
	NKS = 300
	delta = 0.001

	fig = figure(figsize=(8, 6))
	ax = fig.add_subplot(1,1,1)
	
	title(r'simulation ($10^5$ samples)',fontsize=16,y=1.05)
	
	xlabel(r'test statistic $C_1/C_0$',fontsize=16)
	ylabel(r'number of samples',fontsize=16)
	
	ax.tick_params(axis='both',which='both',direction='in')
	
	for tick in ax.xaxis.get_major_ticks() :
		tick.label.set_fontsize(16) 
   	
	for tick in ax.yaxis.get_major_ticks() :
		tick.label.set_fontsize(16)  
	
	xlim([0,0.3])
	ylim([0.1,1e5])
	
	
	hist(KS1,bins=np.arange(0,NKS*delta,delta),log=True,alpha=0.4,color="red",label=r'isotropic / $N_{\rm tot}=100$')
	hist(KS2,bins=np.arange(0,NKS*delta,delta),log=True,alpha=0.4,color="green",label=r'dipole / $N_{\rm tot}=100$')
	TS = []
	chi2 = []

	med1 = np.median(KS1)
	med2 = np.median(KS2)
	plot(np.array([med1,med1]),np.array([0.01,1e5]),color="black",linestyle="dotted")
	plot(np.array([med2,med2]),np.array([0.01,1e5]),color="black",linestyle="dotted")
	
	leg = plt.legend(bbox_to_anchor=(0.95, 0.95), loc=1, borderaxespad=0.,fancybox=False,framealpha=0.0,frameon=True,numpoints=1, scatterpoints = 1,handlelength=1)
	for t in leg.get_texts() :
		t.set_fontsize(14)
	
	savefig("C1_test.pdf",bbox_inches = 'tight');
	close()

		
		