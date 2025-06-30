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
#  Author: Troels C. Petersen (NBI)
#  Email:  petersen@nbi.dk
#  Date:   14th of March 2016
# ------------------------------------------------------------------------ #

from ROOT import *
from array import array
import math
import sys
from numpy import matrix
from numpy import linalg

gStyle.SetOptStat("emr")
gStyle.SetOptFit(1111)

SavePlots = False
verbose = True
Nverbose = 10
RunFast = False    # Fix PDF shape parameters to truth values!

pi = TMath.Pi()


# ----------------------------------------------------------------------------------- #
# Functions:
# ----------------------------------------------------------------------------------- #
def sqr( a ) : return a*a



# ------------------------------------------------------------------------ #
def main() : 
# ------------------------------------------------------------------------ #

    # File with data in:
    infile = open('data_sWeights.txt', 'r')

    # List (size 3 x Nevents) to put data into:
    x_all = []

    # Number of variables and definition of 1D histogram sizes:
    Nvar = 3
    Nbins = [ 100,  100,  100]
    xmin  = [ 0.0, -3.0, -1.0]
    xmax  = [ 2.0,  2.0,  1.0]
    VarName = ["Mass", "Shape", "Angle"]
    hist_all = [TH1D("hist_all_" + VarName[ivar], ";" + VarName[ivar] + ";Frequency", Nbins[ivar], xmin[ivar], xmax[ivar]) for ivar in xrange(Nvar)]

    # 2D histograms:
    hist2D_all = TH2D("hist2D_all", ";Mass;Shape", Nbins[0], xmin[0], xmax[0], Nbins[1], xmin[1], xmax[1])

    # Calculating binwidth to ensure that PDFs are normalised correctly:
    binwidth0 = (xmax[0] - xmin[0]) / Nbins[0]
    binwidth1 = (xmax[1] - xmin[1]) / Nbins[1]
    binarea = binwidth0 * binwidth1


    # ------------------------------------------------------------------------------
    # Read in the data points with 3 variables. Shapes for signal and background are:
    #  * Mass:  Gaussian peak vs. exponential.
    #  * Shape: Two Gaussian peaks.
    #  * Angle: Two Beta distributions.
    # ------------------------------------------------------------------------------

    Nevents = 0

    # Loop over the file and read variables:
    for line in infile:
        line = line.strip()              # Remove all "strange" characters
        columns = line.split()           # Split the line into its parts (columns is now a list)
        if (len(columns) == 3) :         # Check that there are exactly three numbers!

            # Record (and print) the measurements:
            x = [float(columns[0]), float(columns[1]), float(columns[2]) ]
            x_all.append(x)
            if (verbose and Nevents < Nverbose) :
                print "  %7.3f    %7.3f    %7.3f  "%(x_all[-1][0], x_all[-1][1], x_all[-1][2])

            # Fill histograms and count events:
            for i in xrange( Nvar ) : hist_all[i].Fill(x_all[-1][i])
            hist2D_all.Fill(x_all[-1][0], x_all[-1][1])
            Nevents += 1
 
    infile.close()



    # Fit the signal and background samples in 1D:
    # --------------------------------------------
    # Fit mass dimension:
    def func_GaussExp(x, p) :
        z = (x[0] - p[1]) / p[2]
        sig = p[0]*binwidth0 / sqrt(2.0*pi)/p[2] * exp(-0.5*z*z)
        bkg = p[3]*binwidth0 * p[4] * exp(-p[4]*x[0])
        return sig+bkg

    fit_mass = TF1("fit_mass", func_GaussExp, 0.0, 2.0, 5)
    fit_mass.SetParameters(4000.0, 1.0, 0.2, 11000.0, 0.5)
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
    fit_shape.SetParameters(4000.0, 0.0, 0.4, 11000.0, -1.0, 0.6)
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
    fitres = hist2D_all.Fit("fit_massshape", "LRS")   # Option "S" gives fit result as output!
    cmfit = fitres.GetCovarianceMatrix()              # Access to entries: cmfit[0][0]

    

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

    canvas1.cd(4)
    hist2D_all.SetMarkerColor(kMagenta)
    hist2D_all.Draw("box")

    canvas1.Update()
    if (SavePlots) : canvas1.SaveAs("VariableDistributions.pdf")



    # -----------------------------------------------------------------------------------
    # Given succesful fit, how do you determine what the signal distribution of "angle" is?
    # -----------------------------------------------------------------------------------

    # Here are empty histograms - try to fill them:
    hist_Angle_sig = TH1D("hist_Angle_sig", ";Signal Angle;Frequency", Nbins[2], xmin[2], xmax[2])
    hist_Angle_bkg = TH1D("hist_Angle_bkg", ";Background Angle;Frequency", Nbins[2], xmin[2], xmax[2])


    """
    for i in xrange ( len(x_all) ) :
        hist_Angle_sig.Fill( SOMETHING )
        hist_Angle_bkg.Fill( SOMETHING )


    # Produce plots with the variable distributions for signal and background:
    # ------------------------------------------------------------------------
    canvas2 = TCanvas("canvas2", "", 50, 50, 1200, 700)
    canvas2.Divide(1,2)

    canvas2.cd(1)
    hist_Angle_sig.SetLineColor(kRed)
    hist_Angle_sig.SetLineWidth(2)
    hist_Angle_sig.Draw("e")

    canvas2.cd(2)
    hist_Angle_bkg.SetLineColor(kBlue)
    hist_Angle_bkg.SetLineWidth(2)
    hist_Angle_bkg.Draw("e")

    canvas2.Update()
    if (SavePlots) : canvas2.SaveAs("AngleDistributions.pdf")
    """


    raw_input( ' ... ' )
    return 


# ------------------------------------------------------------------------ #
if __name__ == '__main__':
    sys.exit( main() )



# ----------------------------------------------------------------------------------- #
#
# Start by taking a look at the data and the 1D fits to ensure that you understand
# what is going on. Then inspect the 2D fit, and see if you understand how this is
# constructed.
#
# Questions:
# ----------
#  1) Do the two 1D fits and the 2D fit converge well? Do they have good Chi2 probabilities?
#     Can you imagine what the signal and background distributions look like? Otherwise draw them!
#
#  2) Try to make a signal and a background selection in Mass and Shape, and plot these to get a
#     feel for the signal and background distributions of the Angle variables. Then try to subtract
#     the (correctly estimated) amount of background from the signal Angle distribution, such that
#     it yields an estimate of the true signal distribution.
#     Additionally or alternatively, calculate a weight as PDFsignal / (PDFsignal + PDFbackground)
#     for each event, and see if it compares to the background subtracted estimate from above.
#
#  3) Now try to calculate an sWeight from the PDF value and the covariance matrix. Follow the
#     recipe in the paper (http://arxiv.org/pdf/physics/0402083v3.pdf) page 12, also described in
#     the slides.
