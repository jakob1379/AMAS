# Classes

Class notes will be posted here:

---

## 0 - Pre-Course

* Take a look before the class starts (optional)
* Get a preview with the course Teaching Assistant (Jean-Loup Tastet) of some software tools to install
* [Lecture 0](Slides/Lecture0_PreTest.pdf)

---

## 1 - Start (Feb. 5)

* [Course Information](Slides/CourseInformation.pdf)
* [description in Kurser](http://kurser.ku.dk/course/nfyk15002u/2018-2019)
* Chi-square
* Code chi-square
* Data for exercise 1 ([FranksNumbers.txt](data/FranksNumbers.txt))
* Review of 'basic' statistics
* [Lecture 1](Slides/Lecture1_Basics_ChiSquare.pdf)
    * Jason's [python code](Exercises/Lecture1_Variance.py) for exercise 1
    * Jean-Loup's (2019 TA) [python 3 code as a Jupyter notebook](Exercises/Lecture1_Variance_Py3.ipynb) for exercise 1
* Be knowledgeable about the Central Limit Theorem
* Start reading paper about how well Gaussian statistics compares to a wide selection of scientific measurements
    * "Not Normal: the uncertainties of scientific measurements" link at [arXiv](https://arxiv.org/abs/1612.00778) or [DOI](http://rsos.royalsocietypublishing.org/content/4/1/160600)
    * We will be discussion the paper in the next class, i.e. on Thursday

---

## 2 - Monte Carlo Simulation & Least Squares (Feb. 7)

* [Lecture 2](Slides/Lecture2_MC_LeastSquares.pdf)
* Monte Carlo (reminder that lecture starts at 09:00)
* Code for [area of the circle](Exercises/Lecture2_CircleArea.py)
* [Example code](Exercises/Lecture2_CircleArea_Py3.ipynb) from Jean-Loup (2019 TA) in a Jupyter notebook
* From the "Not Normal: the uncertainties of scientific measurements" [paper](https://arxiv.org/abs/1612.00778):
    * For the ambitious, create a 'toy monte carlo' of the sample and pair distributions for the nuclear physics data in Sec. 2.A. For simplicity assume that all the 'quantities' are gaussian distributed
    * Write functions where you can produce multiple gaussian distributions to sample from and generate a sample of "12380 measurements, 1437 quantities, 66677 pairs".
    * Produce the z-distribution (using eq. 4) plot for just your toy monte carlo and see if it matches a gaussian, exponential, student-t distribution, etc...
* Least Squares lecture (starting at 13:00)
* Some useful links
    * [Covariance Matrix (wiki)](https://en.wikipedia.org/wiki/Covariance_matrix)
    * [In-Depth (but still brief) least-squares write-up](http://stat.ethz.ch/~geer/bsa199_o.pdf)
* Discussion of "Not Normal: the uncertainties of scientific measurements" ([arXiv](https://arxiv.org/abs/1612.00778) or [DOI](http://rsos.royalsocietypublishing.org/content/4/1/160600))

---

## 3 - Introduction to Likelihoods and Numerical Minimizers (Feb. 12)

* [Lecture 3](Slides/Lecture3_General_Likelihood.pdf)
* Maximum likelihood method
* Gradient descent and minimizers
* Example code for [exercise 1](Exercises/Lecture3_Exercise1.ipynb) and [exercises 2 & 3](Exercises/Lecture3_Exercises2-3.ipynb) from Jean-Loup (TA in 2018 & 2019), [Niccolo](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2018/Exercises/Lecture3_likelihood_niccolo.py) (TA in 2017), some from [Jason](Exercises/Lecture3_MLE_Cowan_clean.py) (course lecturer)
* Remember that the first assignment is due on **Wednesday**

---

## 4 - Intro. to Bayesian Statistics & Splines (Feb. 14)

* [Lecture 4](Slides/Lecture4_Bayes.pdf) on Simple Bayesian statistics
* Using priors, posteriors, and likelihoods
* Example [code](Exercises/Lecture4_Bayes_1.py) for exercises from Jason
* [Lecture 4.5](Slides/Lecture4.5_Splines.pdf)
* Splines
* Data files for one of the exercises.
    * [Dust Logger data](data/DustLog_forClass.dat)
    * [Spline cubic data](data/SplineCubic.txt)
    * [Spline oscillation data](data/SplineOsc1.txt)
* Interesting article about use of splines and penalty terms
    * [Penalized splines](https://arxiv.org/pdf/1301.2184v1.pdf)

---

## 5 - Parameter Estimation and Confidence Intervals (Feb. 19)

* [Lecture 5](Slides/Lecture5_ConfidenceIntervals.pdf) Confidence intervals
* Numerical minimizers for best-fit values
* [Data file](http://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2016/Exercises/MLE_Variance_data.txt) for one of the exercises ([extra data file](data/MLE_Variance_data_2.txt))
* Reminder: oral presentation and 1-2 page article reports will be due/covered soon
    * [Article about Supernova](https://arxiv.org/abs/1701.02596) first detection time. Look at the caption for the Supplementary Fig. 8

---

## 6 - Markov Chain(s) (Feb. 21)

* Look for an external package for Markov Chain Monte Carlo (MCMC), e.g. emcee, PyMC
    * Just like minimizers, syntax and options matter
    * Be familiar with your chosen MCMC package
* [Lecture 6](Slides/Lecture6_MCMC_Bayes.pdf) Markov Chain Monte Carlo (MCMC)
* Some example python code for the exercises (caveat emptor)
    * [Using PyMC](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture6_MCMC_Example.py), which wasn't the greatest package (at least in 2017 and 2018), but it got the job done
    * [Using emcee](https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exercises/Lecture6_MCMC_Example1_Niccolo.py), the solution is graciously provided by Niccolo Maffezzoli (2017 TA)

---

## 7 - Hypothesis Testing (Feb. 26)

* [Lecture 7](Slides/Lecture7_HypothesisTests.pdf)
* Likelihood ratio
* Data files for one of the exercises. Just use the first column in each file. The second column is unimportant.
    * [Data set 1](data/Lecture8_LLH_Ratio_2_data.txt)
    * [Data set 2](data/Lecture8_LLH_Ratio_2a_data.txt)

---

## 8 - Data Driven Density Estimation (non-parametric) (Feb. 28)

* Kernel Density estimation
* [Lecture 8](Slides/Lecture8_KDE.pdf)

---

## 9 - Confidence Intervals, Failures, and Feldman-Cousins (March 5)

* [Guest lecture](Slides/FC2019.pdf) by Dr. Morten Medici
* Under/over coverage in hypothesis tests
* Flip-flopping confidence intervals and corrections via ranking and use of Feldman-Cousins unified approach
    * [Paper](https://arxiv.org/abs/physics/9711021) about unified approach by G. Feldman and R. Cousins

---

## 10 - Presentations and Multivariate Analysis techniques (March 7)

* In the morning we will have the oral presentations from the articles chosen
    * Link to some of the [2019](StudentPresentations.md) presentations
    * Links to some to some of the presentations ([2016](../../2016/classes/#10-oral-presentations-in-class-non-parametric-tests), [2017](../../2017/classes/#10-presentations-and-multivariate-analysis-techniques), [2018](../../2018/StudentPresentations2018/))
    
The Boosted Decision Tree lecture will be covered on March 14 in the afternoon due to the length of the excellent in-class student presentations and follow-up discussions.

---

## 11 - Divergence Between Distributions and Template Matching (March 12)

* Guest Lecture by Prof. Andrew "Andy" Jackson
* Lecture notes on Kullback-Leiber (part 1) and Template Matching (part 2) ([PDF](Slides/KLjason_lecture.pdf), [powerpoint](Slides/KLjason_lecture.pptx))
* Kullback-Leibler divergence as a way to compare the sameness (or tension) of two distributions, also known as a 'measure of surprise' or 'relative entropy'.
    * Kullback-Leibler [exercises](Slides/KLjason-1.pdf)
    * Relevant Publications:
        * Original publication by [Kullback & Leibler](https://doi.org/10.1214%2Faoms%2F1177729694)
        * Application of Kullback-Leibler divergence for properties of the [Cosmic Microwave Background](https://iopscience.iop.org/article/10.1088/1475-7516/2015/06/051/meta)
* Strict, or semi-strict, template matching compares data to predetermined 'templates'. Shortcomings of this approach will be covered.

---

## 12 - Statistical Hypothesis Tests, Auto-Correlation, and BDTs (March 14)

* Guest lecture by Markus Ahlers
    * [Lecture slides](Slides/Lecture_Ahlers2019.pdf)
    * Files and some example code
        * Data files in .FITS format: [eventmap1.fits](data/eventmap1.fits) and [truemap1.fits](data/truemap1.fits)
        * Some example code (all in python): [C1_produce.py](Exercises/C1_produce.py) [C1_show.py](Exercises/C1_show.py) [KS_produce.py](Exercises/KS_produce.py) [KS_show.py](Exercises/KS_show.py) [maxLH_produce.py](Exercises/maxLH_produce.py) [maxLH_show.py](Exercises/maxLH_show.py) [powerspectrum.py](Exercises/powerspectrum.py) [twopoint.py](Exercises/twopoint.py) [Ylm.py](Exercises/Ylm.py)
    * **Be sure** to have [HEALPix software](https://healpix.jpl.nasa.gov) installed on your computer. There are options for C, C++, JAVA, Python, and I see some MATLAB too.
* Boosted Decision Trees
    * [Lecture 10](Slides/Lecture10_MVA.pdf)
    * Data
        * Exercise 1 ([training signal](data/BDT_signal_train.txt), [training background](data/BDT_background_train.txt), [testing signal](data/BDT_signal_test.txt), [testing background](data/BDT_background_test.txt))
        * Exercise 2 (16 variable [file](data/BDT_16var.txt))
            * The first column is the index, hence there are 17 'variables', but the index variable only for book keeping and has no impact on whether an event is signal or background.
            * Every even row is the 'signal' and every odd row is the 'background'. Thus, there are two rows for each index in the first column: the first is the signal and the second is the background. [Format is odd, but I got it from a colleague].
        * Here is the solution data sets separated into two files ([benign](data/benign_true.txt) and [malignant](data/malignant_true.txt)) for the last exercise of the lecture. Here is also the [(python) code](Exercises/Exam2_Problem_BDT_CheckSolutions_2016.py) that I used to establish the efficiency for all the submissions from all the students

---

## 13 - Nested Sampling, Bayesian Inference, and MultiNest (March 19)

* [Lecture 13](Slides/Lecture13_MultiNest.pdf)
* External packages for conducting nested sampling, e.g. MultiNest, are necessary and some python options are:
    * pymultinest ([https://johannesbuchner.github.io/PyMultiNest/](https://johannesbuchner.github.io/PyMultiNest/))
    * nestle ([http://kbarbary.github.io/nestle/](http://kbarbary.github.io/nestle/))
    * SuperBayeS ([http://www.ft.uam.es/personal/rruiz/superbayes/?page=main.html](http://www.ft.uam.es/personal/rruiz/superbayes/?page=main.html))
* Very good articles that are easy to read
    * Excellent and readable paper by developer John Skilling on nested sampling ([http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf](http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf))
        * Read up until the section "The Density of States". There will be a **discussion at the end of class**.
    * MultiNest academic papers
        * [http://arxiv.org/abs/0809.3437](http://arxiv.org/abs/0809.3437)
        * [http://arxiv.org/abs/1306.2144](http://arxiv.org/abs/1306.2144)

---

## 14 - Work on Project (March 21)

* No lecture or new material.

---

## 15 - Course Review, Discussion on Frequentist and Bayesian concepts, and Non-Parametric Tests Lecture snippet (March 26)

* [Review and recap](Slides/Lecture_Review.pdf) of a few topics covered in the course
* [Lecture 15](Slides/Lecture15_Nonparameteric.pdf) (EXTRA)
    * Kolmogorov-Smirnov, Anderson-Darling, and Mann-Whitney U tests
    * *Won't be be covered in class*
    * Topics include things that may be useful for research

---

Extra Projects of a more difficult nature, for those who want something more challenging.

* [Parameter Goodness-of-fit](Slides/ProblemFromMIT.pdf) (PG) in Global physics fits
