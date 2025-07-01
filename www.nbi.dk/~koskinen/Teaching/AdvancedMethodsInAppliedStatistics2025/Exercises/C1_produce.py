#!/usr/local/bin/python3

import healpy as H
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import pickle

if __name__ == "__main__":

	my_cmap = cm.Greys
	my_cmap.set_under("w")
	
	rc('text', usetex=True)
	rc('font',**{'family':'serif','serif':['Palatino']})
	# resolution of output maps
	nside = 32
	npix = H.nside2npix(nside)
	
	RUNS = 100000
	Ntot = 100
	
	C1 = []
	
	for run in range(0,RUNS) :
	
		print(run)
		
		map = np.zeros(npix,dtype=np.int)
	
		for i in range(0,Ntot) :
			phitemp = np.random.rand()*2*np.pi
			x = np.random.rand()
		
			# dipole anisotropy :
			ani = 0.9
			costhetatemp = (1.-np.sqrt(1.0+2.*ani+ani**2-4.*ani*x))/ani
		
			#isotropic :
			#costhetatemp = 2.0*x-1.0
		
			thetatemp = np.arccos(costhetatemp)
		
			pixel = H.ang2pix(nside,thetatemp,phitemp)
			map[pixel] += 1.0
			
		map = map/(1.*Ntot)
		
		LMAX = 30
		
		out = H.anafast(map,alm=True,lmax=LMAX)	
		
		C1.append(out[0][1]/out[0][0])
		
	pickle.dump(C1,open('C1dipole_Ntot100_Nsample10000.dat', "bw" ))	
	
	hist(C1,bins=100)
	show()
	