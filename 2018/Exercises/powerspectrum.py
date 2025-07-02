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

	nside = 64
	npix = H.nside2npix(nside)

	RUNS = 1000
	LMAX = 40
	
	map = H.read_map('truemap1.fits')
	H.mollview(map,title='template map (Poisson mean per pixel)')
	H.graticule()
	savefig("truemap.pdf",bbox_inches = 'tight');
	close()
	
	eventmap = H.read_map('eventmap1.fits')
	totevents = sum(eventmap)
	H.mollview(eventmap,title='data map with ' + str(totevents) + ' events')
	H.graticule()
	savefig("datamap.pdf",bbox_inches = 'tight');
	close()
	
	out = H.anafast(map,alm=True,lmax=LMAX)	
	Cltrue = out[0]/out[0][0] # normalize by C0
		
	out = H.anafast(eventmap,alm=True,lmax=LMAX)	
	Clobs = out[0]/out[0][0]  # normalize by C0
	
	Clbg = np.zeros((RUNS,LMAX+1),dtype=np.double)
	
	Nscramble = 2*npix
	
	for run in range(0,RUNS) :
		print(run)
		
		for s in range(0,Nscramble) :
		
			# pick two random bins in event map
			i = np.random.randint(0,npix)
			j = np.random.randint(0,npix)
		
			# interchange bins
			temp = eventmap[i] 
			eventmap[i] = eventmap[j]
			eventmap[j] = temp
	
		#
		out = H.anafast(eventmap,alm=True,lmax=LMAX)	
		Clbg[run] = out[0]/out[0][0]
	
	Cl5 = np.zeros(LMAX+1,dtype=np.double)
	Cl50 = np.zeros(LMAX+1,dtype=np.double)
	Cl95 = np.zeros(LMAX+1,dtype=np.double)
	
	temp = np.transpose(Clbg)
	for i in range(0,LMAX+1) :
		Cl5[i] = np.percentile(temp[i],5.0)
		Cl50[i] = np.percentile(temp[i],50.0)
		Cl95[i] = np.percentile(temp[i],95.0)
	
	fig = figure(figsize=(8, 6))
	ax = fig.add_subplot(1,1,1)
	
	
	xlabel(r'$\ell$',fontsize=16)
	ylabel(r'normalized power spectrum $C_\ell/C_0$',fontsize=16)
	
	ax.tick_params(axis='both',which='both',direction='in')
	
	for tick in ax.xaxis.get_major_ticks() :
		tick.label.set_fontsize(16) 
   	
	for tick in ax.yaxis.get_major_ticks() :
		tick.label.set_fontsize(16)  
	
	xlim([0,20])
	
	ax.set_yscale('log')
	
	x = np.arange(1,21,1)	
	scatter(x,Cltrue[1:21],color='red',label=r'input map')
	scatter(x,Clobs[1:21],color='green',label=r'event map')
	plot(x,Cl50[1:21],color='gray',label=r'noise (90\% central)')
	ax.fill_between(x,Cl5[1:21],Cl95[1:21],color='gray',alpha=0.5)
	plot(x,1./totevents*x**0,color='black',linestyle='dotted',label=r'$1/N_{\rm tot}$')
	
	leg = plt.legend(bbox_to_anchor=(0.95, 0.95), loc=1, borderaxespad=0.,fancybox=False,framealpha=0.0,frameon=True,numpoints=1, scatterpoints = 1,handlelength=1)
	for t in leg.get_texts() :
		t.set_fontsize(14)
	
	savefig("Cl_data_vs_bgr.pdf",bbox_inches = 'tight');
	close()
	

