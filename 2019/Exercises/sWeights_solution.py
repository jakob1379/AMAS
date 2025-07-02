#!/usr/bin/env python

# ------------------------------------------------------------------------ #
#  Program for illustrating the use of sWeights from multidimensional fits.
# 
#  Challenge at hand:
#    Given uncorrelated multidimensional data of two (or more) different
#    categories (e.g. signal and background), which can be fitted in some
#    dimensions (separation variables), how to best estimate the distribution
#    of other variables (control variables) of interest for a specific
#    category (typically signal)?
# 
#  This is a very general problem. Imagine you have two (or more) types of
#  mice, bacteria, cells, particles, humans, etc., and that you don't know
#  which are of which type in general, but only from a known feature, such
#  as size, shape, color, income, activity, etc. which you can fit.
#  Now you want to know the distribution of another feature for one type
#  of cells, etc. - how to get this, along with the correct uncertainties?
# 
#  Author: Troels C. Petersen (NBI)
#  Email:  petersen@nbi.dk
#  Date:   18th of February 2018
# ------------------------------------------------------------------------ #

from ROOT import *
from array import array
import math
import sys
from numpy import matrix
from numpy import linalg

gStyle.SetOptStat("emr")
gStyle.SetOptFit(1111)

r = TRandom3()
r.SetSeed(1)

# Number of events in total:
Nsig =  5000
Nbkg = 10000

SavePlots = True
verbose = True
Nverbose = 10
RunFast = False    # Fix PDF shape parameters to truth values!

pi = TMath.Pi()


# ----------------------------------------------------------------------------------- #
# Functions:
# ----------------------------------------------------------------------------------- #
def sqr( a ) : return a*a


# Beta distribution: f(x) = (1 + a*x + b*x^2) / (2 + 2b/3) for x in [-1,1]
# ----------------------------------------------------------------------------------- #
def betadist(x,a,b) :
    if (abs(x) <= 1.0) : return (1.0 + a*x + b*x*x) / (2.0 + 2.0*b/3.0)
    else               : return 0.0

# Oscillation distribution: f(x) = 1 + A*cos(omega*x + phi) for x in [-1,1]
# ----------------------------------------------------------------------------------- #
def oscdist(x, A, omega, phi) :
    if (abs(A) <= 1.0) : return 1.0 + A*cos(omega*x + phi)
    else               : return 0.0


# Function for generating numbers according to beta distributions:
# ----------------------------------------------------------------------------------- #
def GetAngle( alpha, beta ) :
    if (alpha+beta > 1.0) :
        print "ERROR: alpha and/or beta not in defined range: alpha = %6.2f   beta = %6.2f"%(alpha,beta)
        return -999
    x = -1.0 + 2.0 * r.Uniform()
    y = (1.0+abs(alpha)+abs(beta)) * r.Uniform()
    while (y > betadist(x,alpha,beta)) :
        x = -1.0 + 2.0 * r.Uniform()
        y = (1.0+abs(alpha)+abs(beta)) * r.Uniform()
    return x

# Function for generating numbers according to oscillation distributions:
# ----------------------------------------------------------------------------------- #
def GetAngle2( A, omega, phi ) :
    if (abs(A) > 1.0) :
        print "ERROR: A not in defined range: A = %6.2f"%(A)
        return -999
    x = -1.0 + 2.0 * r.Uniform()
    y = (1.0+abs(A)) * r.Uniform()
    while (y > oscdist(x, A, omega, phi)) :
        x = -1.0 + 2.0 * r.Uniform()
        y = (1.0+abs(A)) * r.Uniform()
    return x



# ------------------------------------------------------------------------ #
def main() : 
# ------------------------------------------------------------------------ #

    outfile = open('output.txt', 'w')

    # Define lists and histograms (fast running):
    # x_sig = [ array('f', [0.0, 0.0, 0.0] ) for _ in xrange(Nsig) ]
    # x_bkg = [ array('f', [0.0, 0.0, 0.0] ) for _ in xrange(Nbkg) ]
    # x_all = [ array('f', [0.0, 0.0, 0.0] ) for _ in xrange(Nsig+Nbkg) ]
    # Define lists and histograms (fast coding):
    x_sig = []
    x_bkg = []
    x_all = []

    # Number of variables and definition of 1D histogram sizes:
    Nvar = 3
    Nbins = [ 100,  100,  100]
    xmin  = [ 0.0, -3.0, -1.0]
    xmax  = [ 2.0,  2.0,  1.0]
    VarName = ["Mass", "Shape", "Angle"]
    hist_sig = [TH1D("hist_sig_" + VarName[ivar], ";" + VarName[ivar] + ";Frequency", Nbins[ivar], xmin[ivar], xmax[ivar]) for ivar in xrange(Nvar)]
    hist_bkg = [TH1D("hist_bkg_" + VarName[ivar], ";" + VarName[ivar] + ";Frequency", Nbins[ivar], xmin[ivar], xmax[ivar]) for ivar in xrange(Nvar)]
    hist_all = [TH1D("hist_all_" + VarName[ivar], ";" + VarName[ivar] + ";Frequency", Nbins[ivar], xmin[ivar], xmax[ivar]) for ivar in xrange(Nvar)]

    # 2D histograms:
    hist2D_sig = TH2D("hist2D_sig", ";Mass;Shape", Nbins[0], xmin[0], xmax[0], Nbins[1], xmin[1], xmax[1])
    hist2D_bkg = TH2D("hist2D_bkg", ";Mass;Shape", Nbins[0], xmin[0], xmax[0], Nbins[1], xmin[1], xmax[1])
    hist2D_all = TH2D("hist2D_all", ";Mass;Shape", Nbins[0], xmin[0], xmax[0], Nbins[1], xmin[1], xmax[1])

    # Calculating binwidth to ensure that PDFs are normalised correctly:
    binwidth0 = (xmax[0] - xmin[0]) / Nbins[0]
    binwidth1 = (xmax[1] - xmin[1]) / Nbins[1]
    binarea = binwidth0 * binwidth1


    # ------------------------------------------------------------------------------
    # Produce the desired number of points with 3 variables for signal and background:
    #  * Mass:  Gaussian peak vs. exponential.
    #  * Shape: Two Gaussian peaks.
    #  * Angle: Beta distribution.
    # ------------------------------------------------------------------------------

    # Produce mass, shape and angle values for signal:
    for isig in xrange ( Nsig ) :

        # x_sig.append( [ r.Gaus(  0.8, 0.2 ), r.Gaus(  0.0, 0.4 ), GetAngle( 0.8, 0.2 ) ] )
        # x_all.append( [ r.Gaus(  0.8, 0.2 ), r.Gaus(  0.0, 0.4 ), GetAngle( 0.8, 0.2 ) ] )
        x_sig.append( [ r.Gaus(  0.8, 0.2 ), r.Gaus(  0.0, 0.4 ), GetAngle2( 0.9, 12.0, 1.0 ) ] )
        x_all.append( [ r.Gaus(  0.8, 0.2 ), r.Gaus(  0.0, 0.4 ), GetAngle2( 0.9, 12.0, 1.0 ) ] )
        for i in xrange( Nvar ) :
            hist_sig[i].Fill(x_sig[-1][i])
            hist_all[i].Fill(x_sig[-1][i])
        hist2D_sig.Fill(x_sig[-1][0], x_sig[-1][1])
        hist2D_all.Fill(x_sig[-1][0], x_sig[-1][1])

        # Write to output file (in ASCII):
        for i in xrange( Nvar ) : outfile.write( " %8.4f"%(x_sig[-1][i]) ),
        outfile.write("\n")
        if (verbose and isig < Nverbose) :
            print "  Signal:    ",
            for i in xrange( Nvar ) : print "  var%1d: %6.3f"%(isig, x_sig[-1][i]),
            print

        
    # Produce mass, shape and angle values for signal:
    for ibkg in xrange ( Nbkg ) :

        # x_bkg.append( [ r.Exp( 0.5 ), r.Gaus( -1.0, 0.6 ), GetAngle( -0.8, 0.2 ) ] )
        # x_all.append( [ r.Exp( 0.5 ), r.Gaus( -1.0, 0.6 ), GetAngle( -0.8, 0.2 ) ] )
        x_bkg.append( [ r.Exp( 0.5 ), r.Gaus( -1.0, 0.6 ), GetAngle2( 0.8, 17.0, 0.5 ) ] )
        x_all.append( [ r.Exp( 0.5 ), r.Gaus( -1.0, 0.6 ), GetAngle2( 0.8, 17.0, 0.5 ) ] )
        for i in xrange( Nvar ) :
            hist_bkg[i].Fill(x_bkg[-1][i])
            hist_all[i].Fill(x_bkg[-1][i])
        hist2D_bkg.Fill(x_bkg[-1][0], x_bkg[-1][1])
        hist2D_all.Fill(x_bkg[-1][0], x_bkg[-1][1])

        # Write to output file (in ASCII):
        for i in xrange( Nvar ) : outfile.write( " %8.4f"%(x_bkg[-1][i]) ),
        outfile.write("\n")
        if (verbose and ibkg < Nverbose) :
            print "  Background:",
            for i in xrange( Nvar ) : print "  var%1d: %6.3f"%(ibkg, x_bkg[-1][i]),
            print
 
    outfile.close()



    # Fit the signal and background samples in 1D:
    # --------------------------------------------
    # Fit mass dimension:
    def func_GaussExp(x, p) :
        z = (x[0] - p[1]) / p[2]
        sig = p[0]*binwidth0 / sqrt(2.0*pi)/p[2] * exp(-0.5*z*z)
        bkg = p[3]*binwidth0 * p[4] * exp(-p[4]*x[0])
        return sig+bkg

    fit_mass = TF1("fit_mass", func_GaussExp, 0.0, 2.0, 5)
    fit_mass.SetParameters(Nsig, 1.0, 0.2, Nbkg, 0.5)
    fit_mass.SetLineColor(kBlack)
    hist_all[0].Fit("fit_mass", "LR")

    # Fit shape dimension:
    def func_GaussGauss(x, p) :
        zsig = (x[0] - p[1]) / p[2]
        sig = p[0]*binwidth1 / sqrt(2.0*pi)/p[2] * exp(-0.5*zsig*zsig)
        zbkg = (x[0] - p[4]) / p[5]
        bkg = p[3]*binwidth1 / sqrt(2.0*pi)/p[5] * exp(-0.5*zbkg*zbkg)
        return sig+bkg

    fit_shape = TF1("fit_shape", func_GaussGauss, -3.0, 2.0, 6)
    fit_shape.SetParameters(Nsig, 0.0, 0.4, Nbkg, -1.0, 0.6)
    fit_shape.SetLineColor(kBlack)
    hist_all[1].Fit("fit_shape", "LR")


    # Fit the signal and background samples in 2D (mass and shape):
    # ------------------------------------------------------------------------
    def func_GEGG(x, p) :
        z0sig = (x[0] - p[1]) / p[2]
        z1sig = (x[1] - p[3]) / p[4]
        sig = p[0]*binarea / sqrt(2.0*pi)/p[2] * exp(-0.5*z0sig*z0sig) / sqrt(2.0*pi)/p[4] * exp(-0.5*z1sig*z1sig)
        z1bkg = (x[1] - p[7]) / p[8]
        bkg = p[5]*binarea * p[6] * exp(-p[6]*x[0]) / sqrt(2.0*pi)/p[8] * exp(-0.5*z1bkg*z1bkg)
        return sig+bkg
 
    fit_massshape = TF2("fit_massshape", func_GEGG, 0.0, 2.0, -3.0, 2.0, 9)
    # fit_massshape.SetParameters(Nsig, 1.0, 0.2, 0.0, 0.4, Nbkg, 0.5, -1.0, 0.6)
    fit_massshape.SetParameters(fit_mass.GetParameter(0), fit_mass.GetParameter(1), fit_mass.GetParameter(2),
                                fit_shape.GetParameter(1), fit_mass.GetParameter(2), fit_mass.GetParameter(0),
                                fit_mass.GetParameter(1), fit_shape.GetParameter(1), fit_shape.GetParameter(2))
    if (RunFast) :     # For debugging it is worthwhile skipping a 9 parameter fit in 2D!!!
        fit_massshape.FixParameter(1, 1.0)
        fit_massshape.FixParameter(2, 0.2)
        fit_massshape.FixParameter(3, 0.0)
        fit_massshape.FixParameter(4, 0.4)
        fit_massshape.FixParameter(6, 0.5)
        fit_massshape.FixParameter(7,-1.0)
        fit_massshape.FixParameter(8, 0.6)
    fit_massshape.SetLineColor(kBlack)
    hist2D_all.Fit("fit_massshape", "LR")

    # To get the covariance matrix between signal and background normalisations,
    # we fix the shape variables and refit the data:
    fit_massshape2 = TF2("fit_massshape2", func_GEGG, 0.0, 2.0, -3.0, 2.0, 9)
    # fit_massshape2.SetParameters(Nsig, 1.0, 0.2, 0.0, 0.4, Nbkg, 0.5, -1.0, 0.6)
    fit_massshape2.SetParameters(fit_mass.GetParameter(0), fit_mass.GetParameter(1), fit_mass.GetParameter(2),
                                 fit_shape.GetParameter(1), fit_mass.GetParameter(2), fit_mass.GetParameter(0),
                                 fit_mass.GetParameter(1), fit_shape.GetParameter(1), fit_shape.GetParameter(2))
    for ivar in xrange (9) :
        if (ivar != 0 and ivar != 5) :
            fit_massshape2.FixParameter(ivar, fit_massshape.GetParameter(ivar))
    fit_massshape2.SetLineColor(kBlack)
    fitres = hist2D_all.Fit("fit_massshape2", "LRS")      # Option "S" gives fit result as output!
    cmfit = fitres.GetCovarianceMatrix()                  # Only non-zero entries for variable 0 and 5
    covmatfit = matrix( [ [cmfit[0][0], cmfit[0][5]], [cmfit[5][0], cmfit[5][5] ] ] )

    

    # Produce plots with the variable distributions for signal and background:
    # ------------------------------------------------------------------------
    canvas0 = TCanvas("canvas0", "", 20, 20, 1200, 700)

    for i in range ( Nvar ) :
        hist_all[i].SetXTitle(VarName[i])
        hist_all[i].SetYTitle("Frequency")
        hist_all[i].SetMinimum(0.0)
        hist_all[i].SetLineColor(kMagenta)
        hist_all[i].SetLineWidth(2)
        hist_all[i].Draw()
        hist_sig[i].SetLineColor(kRed)
        hist_sig[i].SetLineWidth(2)
        hist_sig[i].Draw("same")
        hist_bkg[i].SetLineColor(kBlue)
        hist_bkg[i].SetLineWidth(2)
        hist_bkg[i].Draw("same")

        canvas0.Update()
        if (SavePlots) : canvas0.SaveAs("DistAll_" + VarName[i] + ".pdf")

    # Get a separate plot of the 2D fit:
    hist2D_all.SetMarkerColor(kMagenta)
    hist2D_all.Draw("box")

    canvas0.Update()
    if (SavePlots) : canvas0.SaveAs("Dist2D_All_fit.pdf")




    # Produce plots with the variable distributions for signal and background:
    # ------------------------------------------------------------------------
    canvas1 = TCanvas("canvas1", "", 20, 20, 1200, 700)
    canvas1.Divide(2,2)

    for i in xrange( Nvar ) : 
        canvas1.cd(i+1)
        hist_all[i].SetXTitle(VarName[i])
        hist_all[i].SetYTitle("Frequency")
        hist_all[i].SetMinimum(0.0)
        hist_all[i].SetLineColor(kMagenta)
        hist_all[i].SetLineWidth(2)
        hist_all[i].Draw()
        hist_sig[i].SetLineColor(kRed)
        hist_sig[i].SetLineWidth(2)
        hist_sig[i].Draw("same")
        hist_bkg[i].SetLineColor(kBlue)
        hist_bkg[i].SetLineWidth(2)
        hist_bkg[i].Draw("same")

    canvas1.cd(4)
    hist2D_all.SetMarkerColor(kMagenta)
    hist2D_all.Draw("box")

    canvas1.Update()
    if (SavePlots) : canvas1.SaveAs("VariableDistributions.pdf")



    # -----------------------------------------------------------------------------------
    # Given succesful fit, calculate sWeights and produce signal distribution of "angle":
    # -----------------------------------------------------------------------------------

    par = []     # Abbreviation of an otherwise very long expression!
    for ipar in xrange ( 9 ) : par.append(fit_massshape.GetParameter(ipar))

    def func_GEGG_signal(x) :
        z0sig = (x[0] - par[1]) / par[2]
        z1sig = (x[1] - par[3]) / par[4]
        return par[0] / sqrt(2.0*pi)/par[2] * exp(-0.5*z0sig*z0sig) / sqrt(2.0*pi)/par[4] * exp(-0.5*z1sig*z1sig)

    def func_GEGG_background(x) :
        z1bkg = (x[1] - par[7]) / par[8]
        return par[5] * par[6] * exp(-par[6]*x[0]) / sqrt(2.0*pi)/par[8] * exp(-0.5*z1bkg*z1bkg)

    # Covariance matrix (inverse to be inverted), calculated from sum over all events:
    iclist = [ [0.0, 0.0], [0.0, 0.0] ]
    for i in xrange ( len(x_all) ) :
        sigPDF = func_GEGG_signal( [x_all[i][0], x_all[i][1] ] ) / par[0]
        bkgPDF = func_GEGG_background( [x_all[i][0], x_all[i][1] ] ) / par[5]
        denominator = sqr( par[0]*sigPDF + par[5]*bkgPDF )
        iclist[0][0] += sigPDF*sigPDF / denominator
        iclist[0][1] += sigPDF*bkgPDF / denominator
        iclist[1][0] += bkgPDF*sigPDF / denominator
        iclist[1][1] += bkgPDF*bkgPDF / denominator
    invcovmat = matrix( [ [iclist[0][0], iclist[0][1]], [iclist[1][0], iclist[1][1]] ] )
    # print "Inverse covarance matrix from direct calculation:  "
    # print invcovmat

    covmat = invcovmat.I
    print "Covarance matrix as obtained from direct calculation: "
    print covmat

    print "Covarance matrix as obtained from fit: "
    print covmatfit

    print "Number of signal events:      %8.1f  (NsigTrue = %5d)"%(par[0], Nsig)
    print "Number of background events:  %8.1f  (NbkgTrue = %5d)"%(par[5], Nbkg)


    # Loop over all events and calculate their sWeight (and background weight = 1-sWeight):
    # Also, use the sWeight in producing plot of signal (and background) angle!
    hist_sWeight_sig = TH1D("hist_sWeight_sig", ";sWeight (for signal events);Frequency", 175, -1.0, 2.5)
    hist_sWeight_bkg = TH1D("hist_sWeight_bkg", ";bWeight (for background events);Frequency", 175, -1.0, 2.5)
    hist_Angle_sig = TH1D("hist_Angle_sig", ";Signal Angle;Frequency", Nbins[2], xmin[2], xmax[2])
    hist_Angle_bkg = TH1D("hist_Angle_bkg", ";Background Angle;Frequency", Nbins[2], xmin[2], xmax[2])

    for i in xrange ( len(x_all) ) :
        sigPDF = func_GEGG_signal( [x_all[i][0], x_all[i][1] ] ) / par[0]
        bkgPDF = func_GEGG_background( [x_all[i][0], x_all[i][1] ] ) / par[5]
        sWeight = (covmat.item(0,0) * sigPDF + covmat.item(0,1) * bkgPDF) / (par[0]*sigPDF + par[5]*bkgPDF)
        bWeight = (covmat.item(1,0) * sigPDF + covmat.item(1,1) * bkgPDF) / (par[0]*sigPDF + par[5]*bkgPDF)
        
        # Plot weights for signal and background events:
        if (i < Nsig) : hist_sWeight_sig.Fill(sWeight)
        else :          hist_sWeight_bkg.Fill(bWeight)
        hist_Angle_sig.Fill(x_all[i][2], sWeight)
        hist_Angle_bkg.Fill(x_all[i][2], bWeight)

        if ((verbose and i < Nverbose) or (verbose and i >= Nsig and i < Nsig+Nverbose)) :
            print "  %4d:   m=%6.3f  s=%6.3f   sigPDF=%6.3f  bkgPDF=%6.3f   s/bWeight = %6.3f %6.3f"%(i,x_all[i][0],x_all[i][1],sigPDF,bkgPDF,sWeight,bWeight)


    # Produce plots with the variable distributions for signal and background:
    # ------------------------------------------------------------------------
    canvas2 = TCanvas("canvas2", "", 50, 50, 1200, 700)

    hist_sWeight_sig.SetLineColor(kRed)
    hist_sWeight_sig.SetLineWidth(2)
    hist_sWeight_sig.Draw()
    canvas2.Update()
    if (SavePlots) : canvas2.SaveAs("Angle_sWeight.pdf")

    hist_sWeight_bkg.SetLineColor(kBlue)
    hist_sWeight_bkg.SetLineWidth(2)
    hist_sWeight_bkg.Draw()
    canvas2.Update()
    if (SavePlots) : canvas2.SaveAs("Angle_bWeight.pdf")

    hist_Angle_sig.SetLineColor(kRed)
    hist_Angle_sig.SetLineWidth(2)
    hist_Angle_sig.Draw("e")
    hist_sig[2].SetLineColor(kMagenta)
    hist_sig[2].SetLineWidth(2)
    hist_sig[2].Draw("same")
    p_chi2 = hist_sig[2].Chi2Test(hist_Angle_sig, "UW P");
    p_kolm = hist_sig[2].KolmogorovTest(hist_Angle_sig, "N");
    print "  Chi2 and Kolmogorov probability between sPlot and Truth of signal: %6.4f %6.4f"%(p_chi2, p_kolm)
    canvas2.Update()
    if (SavePlots) : canvas2.SaveAs("Angle_signal_sWeights.pdf")

    hist_Angle_bkg.SetLineColor(kBlue)
    hist_Angle_bkg.SetLineWidth(2)
    hist_Angle_bkg.Draw("e")
    hist_bkg[2].SetLineColor(kMagenta)
    hist_bkg[2].SetLineWidth(2)
    hist_bkg[2].Draw("same")
    p_chi2 = hist_bkg[2].Chi2Test(hist_Angle_bkg, "UW P");
    p_kolm = hist_bkg[2].KolmogorovTest(hist_Angle_bkg, "N");
    print "  Chi2 and Kolmogorov probability between sPlot and Truth of background: %6.4f %6.4f"%(p_chi2, p_kolm)
    canvas2.Update()
    if (SavePlots) : canvas2.SaveAs("Angle_background_bWeights.pdf")


    # Produce one plot with everything in (which gives a good overview):
    canvas2.Divide(2,2)

    canvas2.cd(1)
    hist_sWeight_sig.Draw()

    canvas2.cd(2)
    hist_sWeight_bkg.Draw()

    canvas2.cd(3)
    hist_Angle_sig.Draw("e")
    hist_sig[2].Draw("same")

    canvas2.cd(4)
    hist_Angle_bkg.Draw("e")
    hist_bkg[2].Draw("same")

    canvas2.Update()
    if (SavePlots) : canvas2.SaveAs("Angle_PlotOfEverything.pdf")



    raw_input( ' ... ' )
    return 


# ------------------------------------------------------------------------ #
if __name__ == '__main__':
    sys.exit( main() )

