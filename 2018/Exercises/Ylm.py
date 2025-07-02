#!/usr/local/bin/python3

import healpy as H
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

if __name__ == "__main__":

	my_cmap = cm.RdBu_r
	my_cmap.set_under("w")
	
	rc('text', usetex=True)
	rc('font',**{'family':'serif','serif':['Palatino']})

	nside = 128
	npix = H.nside2npix(nside)

	LMAX = 4*nside
	almsize = np.int(((LMAX+2)*(LMAX+1))/2)
	alm = np.zeros(almsize,dtype=np.complex)

	l = 10
	m = 4

	index = H.sphtfunc.Alm.getidx(LMAX,l,m)
	alm[index] = 1.0 # either 1.0 or 1.0j for the two degrees of freedom
	
	map = H.alm2map(alm,nside,lmax=LMAX)
	mapmax = max(max(map),max(-map))
	maptitle = r'$\ell= ' + str(l) + '$ \& $m= ' + str(m) + '$'
	
	H.mollview(map,cmap=cm.RdBu_r,max=mapmax,min=-mapmax,title=maptitle)
	H.graticule()
	show()

	exit(3)