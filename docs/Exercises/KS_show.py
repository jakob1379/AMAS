#!/usr/local/bin/python3

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import pickle

if __name__ == "__main__":
	
	rc('text', usetex=True)
	rc('font',**{'family':'serif','serif':['Palatino']})
	
	RUNS = 100000
	
	KS1 = np.array(pickle.load(open('KSiso_Ntot100_Nsample10000.dat', "br" )))
	KS2 = np.array(pickle.load(open('KSdipole_Ntot100_Nsample10000.dat', "br" )))
	
	NKS = 100
	delta = 0.002

	fig = figure(figsize=(8, 6))
	ax = fig.add_subplot(1,1,1)
	
	title(r'simulation ($10^4$ samples)',fontsize=16,y=1.05)
	
	xlabel(r'$KS$',fontsize=16)
	ylabel(r'number of samples',fontsize=16)
	
	ax.tick_params(axis='both',which='both',direction='in')
	
	for tick in ax.xaxis.get_major_ticks() :
		tick.label.set_fontsize(16) 
   	
	for tick in ax.yaxis.get_major_ticks() :
		tick.label.set_fontsize(16)  
	
	xlim([0,0.2])
	ylim([0.1,1e4])
	
	
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
	
	savefig("KS_test.pdf",bbox_inches = 'tight');
	close()

		
		