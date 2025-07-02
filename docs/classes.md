# Classes

Class notes will be posted here:

---

## 0 - Pre-Course, attendance is not required (Feb. 2, 2017)

*   Optional time to make sure your laptop is setup
*   10:00-12:00 at Blegdamsvej (in Aud. B)
*   [Lecture 0](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture0_PreTest.pdf)

---

## 1 - Start

*   [Course Information](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/CourseInformation.pdf)
*   Chi-square
*   Code chi-square
*   Data for exercise 1 ([FranksNumbers.txt](http://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/data/FranksNumbers.txt))
*   Review of 'basic' statistics
*   [Lecture 1](http://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture1_Basics_ChiSquare.pdf)
    *   Jason's [python code](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture1_Variance.py) for exercise 1
*   Be knowledgeable about the Central Limit Theorem
*   Start reading paper about how well Gaussian statistics compares to a wide selection of scientific measurements
    *   "Not Normal: the uncertainties of scientific measurements" link at [arXiv](https://arxiv.org/abs/1612.00778) or [DOI](http://rsos.royalsocietypublishing.org/content/4/1/160600)
    *   If there's time, there may be discussion on Thurs. about the paper
*   First problem set is [assigned](./index.md#graded-problem-sets)

---

## 2 - Monte Carlo Simulation & Least Squares regression

*   [Lecture 2](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture2_MC_LeastSquares.pdf)
*   Monte Carlo (starting at 09:00)
*   From the "Not Normal: the uncertainties of scientific measurements" [paper](https://arxiv.org/abs/1612.00778):
    *   For the ambitious, create a 'toy monte carlo' of the sample and pair distributions for the nuclear physics data in Sec. 2.A. For simplicity assume that all the 'quantities' are gaussian distributed
    *   Write functions where you can produce multiple gaussian distributions to sample from and generate a sample of "12380 measurements, 1437 quantities, 66677 pairs".
    *   Produce the z-distribution (using eq. 4) plot for just your toy monte carlo and see if it matches a gaussian, exponential, student-t distribution, etc...
*   Least Squares lecture (starting at 13:00)
*   Discussion of the "Not Normal: the uncertainties of scientific measurements" paper

---

## 3 - Introduction to Likelihoods and Numerical Minimizers

*   [Lecture 3](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture3_General_Likelihood.pdf)
*   Maximum likelihood method
*   Gradient descent and minimizers
*   Example code from [Niccolo](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture3_likelihood_niccolo.py) (TA) and some from [Jason](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture3_MLE_Cowan_clean.py) (course lecturer)
*   Remember that the [first assignment](index.md#graded-problem-sets) is due on **Wednesday**

---

## 4 - Finish Introduction Likelihoods and Minimizers, then Intro. to Bayesian Statistics

*   Finish any material from previous class on [likelihoods and minimizers](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture3_General_Likelihood.pdf)
*   [Lecture 4](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture4_Bayes.pdf) on Simple Bayesian statistics
*   Using priors, posteriors, and likelihoods
*   Example [code](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture4_Bayes_1.py) for exercises from Jason

---

## 5 - Background Subtraction and sPlots

*   [Lecture 5](AdvAppStat17_sWeightsAndPlots.pdf) (by Troels Peteresen)
*   [Data file](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/data/data_sWeights.txt) for the exercises
*   Scripts - [sWeights.py](Exercises/sWeights.py) and [sWeights_solution.py](Exercises/sWeights_solution.py)
*   For next class have an external package for Markov Chain Monte Carlo (MCMC), e.g. emcee, PyMC

---

## 6 - Markov Chain(s)

*   Be sure to have an external package for Markov Chain Monte Carlo (MCMC), e.g. emcee, PyMC
    *   Just like minimizers, syntax and options matter
    *   Be somewhat familiar with your chosen MCMC package
*   [Lecture 6](Slides/Lecture6_MCMC_Bayes.pdf) Markov Chain Monte Carlo (MCMC)
*   Some example python code for the exercises (caveat emptor)
    *   [Using PyMC](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture6_MCMC_Example.py), which wasn't the greatest package (at least last year), but it got the job dones
    *   [Using emcee](Exercises/Lecture6_MCMC_Example1_Niccolo.py), the solution is graciously provided by Niccolo Maffezzoli (TA)

---

## 7 - Parameter Estimation and Confidence Intervals

*   [Lecture 7](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture7_ConfidenceIntervals.pdf) Confidence intervals
*   Numerical minimizers for best-fit values
*   [Data file](http://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2016/Exercises/MLE_Variance_data.txt) for one of the exercises
*   [Oral presentation and 1-2 page article reports](index.md#oral-presentation) will be due/covered March 8&9
    *   [Article about Supernova](https://arxiv.org/abs/1701.02596) first detection time. Look at the caption for the Supplementary Fig. 8

---

## 8 - Hypothesis Testing

*   [Lecture 8](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture8_HypothesisTests.pdf)
*   Likelihood ratio
*   Data files for one of the exercises. Just use the first column in each file. The second column is unimportant.
    *   [Data set 1](data/Lecture8_LLH_Ratio_2_data.txt)
    *   [Data set 2](data/Lecture8_LLH_Ratio_2a_data.txt)

---

## 9 - Interpolation and Splines

*   [Lecture 9](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture9_Splines.pdf)
*   Splines
*   Data files for one of the exercises.
    *   [Dust Logger data](data/DustLog_forClass.dat)
    *   [Spline cubic data](data/SplineCubic.txt)
    *   [Spline oscillation data](data/SplineOsc1.txt)
*   Interesting article about use of splines and penalty terms
    *   [Penalized splines](https://arxiv.org/pdf/1301.2184v1.pdf)

---

## 10 - Presentations and Multivariate Analysis techniques

*   In the morning we will have the oral presentations from the articles chosen:
    *   [sFit: a method for background subtraction in maximum likelihood fit](StudentPresentations/Presentation_Tue_Mads.pdf)
    *   [On a paradoxical property of the Kolmogorov-Smirnov two-sample test](StudentPresentations/Presentation_Hasselgren.pdf)
    *   Too good to be true:When overwhelming evidence fails to convince ([PPTX](StudentPresentations/OverwhelmingEvidenceFails.pptx), [PDF](StudentPresentations/OverwhelmingEvidenceFails.pdf)) ([arXiv:1601.00900](https://arxiv.org/abs/1601.00900))
    *   [Bayesian Interpolation](StudentPresentations/Bayesian_Interpolation.pdf) ([Paper](http://www.mitpressjournals.org/doi/pdf/10.1162/neco.1992.4.3.415))
    *   Chempy: A flexible chemical evolution model for abundance fitting ([PDF](StudentPresentations/ChemPy_Presentation.pdf), [ODP](StudentPresentations/ChemPy_Presentation.odp))
*   Boosted Decision Trees
*   [Lecture 10](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture10_MVA.pdf)
*   Exercise 1 TMVA python script (will appear next week)
*   Exercise 2 TMVA python script (will appear next week)
*   Data
    *   Exercise 1 ([training signal](data/BDT_signal_train.txt), [training background](data/BDT_background_train.txt), [testing signal](data/BDT_signal_test.txt), [testing background](data/BDT_background_test.txt))
    *   Exercise 2 (16 variable [file](data/BDT_16var.txt))
        *   The first column is the index, hence there are 17 'variables', but the index variable only for book keeping and has no impact on whether an event is signal or background.
        *   Every even row is the 'signal' and every odd row is the 'background'. Thus, there are two rows for each index in the first column: the first is the signal and the second is the background. [Format is odd, but I got it from a colleague].
    *   Here is the solution data sets separated into two files ([benign](data/benign_true.txt) and [malignant](data/malignant_true.txt)) for the last exercise of the lecture. Here is also the [(python) code](Exam2_Problem_BDT_CheckSolutions_2016.py) that I used to establish the efficiency for all the submissions from all the students

---

## 11 - Data Driven Density Estimation (non-parametric)

*   Kernel Density estimation
*   [Lecture 11](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture11_KDE.pdf)
*   Extra credit is now available (see [here](index.md#extra-credit))
*   Problem set #2 is now assigned (see [here](index.md#graded-problem-sets))

---

## 12 - Confidence Intervals, Failures, and Feldman-Cousins

*   Guest lecture by Dr. Morten Medici
*   Under/over coverage in hypothesis tests
*   Flip-flopping confidence intervals and corrections via ranking and use of Feldman-Cousins unified approach
    *   [Paper](https://arxiv.org/abs/physics/9711021) about unified approach by G. Feldman and R. Cousins
*   [Lecture 12](Slides/FC.pdf)
*   Yes, this topic may appear on the exam :-)
*   I have posted the solution data sets to the webpage for the BDT classification exercise (see links for [Class 10](#10-presentations-and-multivariate-analysis-techniques) above)
*   The due date for the project is now March 27, 2017

---

## 13 - Nested Sampling, Bayesian Inference, and MultiNest

*   [Lecture 13](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture13_MultiNest.pdf)
*   External packages for conducting nested sampling, e.g. MultiNest, are necessary and some python options are:
    *   pymultinest ([https://johannesbuchner.github.io/PyMultiNest/](https://johannesbuchner.github.io/PyMultiNest/))
    *   nestle ([http://kbarbary.github.io/nestle/](http://kbarbary.github.io/nestle/))
    *   SuperBayeS ([http://www.ft.uam.es/personal/rruiz/superbayes/?page=main.html](http://www.ft.uam.es/personal/rruiz/superbayes/?page=main.html))
*   Super awesome articles that are surprisingly easy to read
    *   Excellent and readable paper by developer John Skilling on nested sampling ([http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf](http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf))
    *   MultiNest papers
        *   [http://arxiv.org/abs/0809.3437](http://arxiv.org/abs/0809.3437)
        *   [http://arxiv.org/abs/1306.2144](http://arxiv.org/abs/1306.2144)

---

## 14 - Signal and Data Processing (Wavelets)

*   Guest lecture by Dr. James Monk
*   To prepare for the class make sure that a wavelet package is available
    *   For example in Python - "pip install PyWavelets"
    *   Matlab - http://se.mathworks.com/products/wavelet/
*   [Lecture 14](Slides/Lecture14_Wavelets.pdf)
*   Some coding scripts
    *   Gaussian ([part1](Exercises/Lecture14_wavelet_gaussian_part1.py), [part2](Exercises/Lecture14_wavelet_gaussian_part2.py), [part3](Exercises/Lecture14_wavelet_gaussian_part3.py))
    *   [LIGO](Exercises/Lecture14_wavelet_LIGO.py)
        *   [H-H1_LOSC_4_V1-1126259446-32.txt](data/H-H1_LOSC_4_V1-1126259446-32.txt)
        *   [L-L1_LOSC_4_V1-1126259446-32.txt](data/L-L1_LOSC_4_V1-1126259446-32.txt)

---

## 15 - Non-Parametric Tests Lecture snippet and Course Review

*   Kolmogorov-Smirnov, Anderson-Darling, and Mann-Whitney U tests
*   [Lecture 15](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture15_Nonparameteric.pdf)
*   [Review and recap](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Lecture_Review.pdf) of a few topics covered in the course

---

Extra Projects of a more difficult nature, for those who want something more challenging.

*   [Parameter Goodness-of-fit](Slides/ProblemFromMIT.pdf) (PG) in Global physics fits
