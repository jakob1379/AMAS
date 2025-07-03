# Classes

Class notes will be posted here on this webpage as they become available.

## Optional Software Help Session (Jan. 29)

*   14:00 - 16:30 in NBB 02.3.I.164
*   Optional session with the Teaching Assistant (Preet Bhanjan Pati) for any students who may need assistance with their computer software setup.
*   Get a preview with the course and some software tools to install.

---

## 1 - Start (Feb. 4)

*   [Course Information](Slides/CourseInformation.pdf)
*   Chi-square
*   Code chi-square
*   Data for exercise 1 ([FranksNumbers.txt](data/FranksNumbers.txt))
*   Data for extra part of exercise 1 ([aruj.txt](data/aruj.txt))
*   Review of 'basic' statistics
*   [Lecture 1](Slides/Lecture1_Basics_ChiSquare.pdf)
    *   Jean-Loup's (2019 TA) [python 3 code as a Jupyter notebook](Exercises/Lecture1_Variance_Py3.ipynb) for exercise 1
    *   Tania's (2021 TA) [python 3 code as a Jupyter notebook](Exercises/class1_exercise1.ipynb) for exercise 1
    *   Jason's (2025 code) [Jupyter notebook](Exercises/Lecture1_Variance_DJK.ipynb) for the data from the extra part of exercise 1
*   Start reading paper about how well Gaussian statistics compares to a wide selection of scientific measurements
    *   "Not Normal: the uncertainties of scientific measurements" link at [arXiv](https://arxiv.org/abs/1612.00778) or [DOI](http://rsos.royalsocietypublishing.org/content/4/1/160600)
    *   We will be discussing the paper in the next class, i.e. on Thursday

---

## 2 - Monte Carlo Simulation & Least Squares (Feb. 6)

*   [Lecture 2](Slides/Lecture2_MC_LeastSquares.pdf)
*   Monte Carlo (reminder that lecture starts at 09:00)
*   Code for [area of the circle](Exercises/Lecture2_CircleArea.py). Note that the code is provided for illustrative purposes, and not as a piece of code that students are expected to be able to execute without modification.
*   [Example code](Exercises/Lecture2_CircleArea_Py3.ipynb) from Jean-Loup (2019 TA) in a Jupyter notebook
*   [Example code](Exercises/class2_exercises.ipynb) from Tania (2021 TA) in a Jupyter notebook
*   From the "Not Normal: the uncertainties of scientific measurements" [paper](https://arxiv.org/abs/1612.00778):
    *   For the ambitious, create a 'toy monte carlo' of the sample and pair distributions for the nuclear physics data in Sec. 2.A. For simplicity assume that all the 'quantities' are gaussian distributed.
    *   Write functions where you can produce multiple gaussian distributions to sample from and generate a sample of "12380 measurements, 1437 quantities, 66677 pairs".
    *   Produce the z-distribution (using Eq. 4) plot for just your toy Monte Carlo and see if it matches a gaussian, exponential, student-t distribution, etc...
*   Discussion of "Not Normal: the uncertainties of scientific measurements" ([arXiv](https://arxiv.org/abs/1612.00778) or [DOI](http://rsos.royalsocietypublishing.org/content/4/1/160600))
*   Included here are some [prompt questions](https://alumni-my.sharepoint.com/:w:/g/personal/xdn365_ku_dk/ETtDngnFIw5MtMwkhKDw3FkBKHW8uEgoDcVz5s71CgHGow?e=gegMP6) to accompany discussion and understanding of the paper
*   Least Squares (optional)
*   Some useful links
    *   [Covariance Matrix (wiki)](https://en.wikipedia.org/wiki/Covariance_matrix)
    *   [In-Depth (but still brief) least-squares write-up](http://stat.ethz.ch/%7Egeer/bsa199_o.pdf)

---

## 3 - Introduction to Likelihoods and Numerical Minimizers (Feb. 11)

*   [Lecture 3](Slides/Lecture3_General_Likelihood.pdf)
*   Maximum likelihood method
*   Gradient descent and minimizers
*   Example code for [exercise 1](Exercises/class3_exercise1.ipynb) and [exercise 2-3](Exercises/class3_exercises2-3.ipynb) from Tania (TA in 2021 & 2022), [exercise 1](Exercises/Lecture3_Exercise1.ipynb) and [exercises 2 & 3](Exercises/Lecture3_Exercises2-3.ipynb) from Jean-Loup (TA in 2018 & 2019), [Niccolo](Exercises/Lecture3_likelihood_niccolo.py) (TA in 2017), some from [Jason](Exercises/Lecture3_MLE_Cowan_clean.py) (course lecturer)

---

## 4 - Intro. to Bayesian Statistics & Splines (Feb. 13)

*   [Lecture 4](Slides/Lecture4_Bayes.pdf) on Simple Bayesian statistics
*   Using priors, posteriors, and likelihoods
*   Example [code](Exercises/Lecture4_Bayes_1.py) for exercises from Jason, and [example code](Exercises/class4_bayes.ipynb) from Tania
*   [Lecture 4.5](Slides/Lecture4.5_Splines.pdf)
*   Splines
*   Data files for one of the exercises.
    *   [Dust Logger data](data/DustLog_forClass.dat)
    *   [Spline cubic data](data/SplineCubic.txt)
    *   [Spline oscillation data](data/SplineOsc1.txt)
*   Interesting article about use of splines and penalty terms
    *   [Penalized splines](https://arxiv.org/pdf/1301.2184v1.pdf)

---

## 5 - Parameter Estimation and Confidence Intervals (Feb. 18)

*   [Lecture 5](Slides/Lecture5_ConfidenceIntervals.pdf) Confidence intervals
*   Numerical minimizers for best-fit values
*   [Data file](data/ParameterEstimation_Ex1.txt) for exercise 1 and 2
*   [Data file](data/MLE_Variance_data.txt) for exercise 3 ([extra data file](data/MLE_Variance_data_2.txt))
*   Reminder: oral presentation and 1-2 page article reports will be due soon
    *   [Article about Supernova](https://arxiv.org/abs/1701.02596) first detection time. Look at the caption for the Supplementary Fig. 8

---

## 6 - Markov Chain(s) (Feb. 20)

*   [Lecture 6](Slides/Lecture6_MCMC_Bayes.pdf) Markov Chain Monte Carlo (MCMC)
*   Look for an external package for Markov Chain Monte Carlo (MCMC), e.g. emcee
    *   Just like minimizers, syntax and options matter
    *   Be familiar with your chosen MCMC package
*   Some example python code for the exercises (caveat emptor)
    *   [Using emcee](Exercises/Lecture6_MCMC_Example1_Niccolo.py), the solution is graciously provided by Niccolo Maffezzoli (2017 TA)

---

## 7 - Hypothesis Testing (Feb. 25)

*   [Lecture 7](Slides/Lecture7_HypothesisTests.pdf)
*   Likelihood ratio
*   Data files for one of the exercises. Just use the first column in each file. The second column is unimportant.
    *   [Data set 1](data/LLH_Ratio_2_data.txt)
    *   [Data set 2](data/LLH_Ratio_2a_data.txt)

---

## 8 - Kernel Density Estimator (Feb. 27)

*   [KDE Lecture Slides](Slides/Lecture8_KDE.pdf)
*   In the afternoon there is time to work on the Presentation and/or Project write-up.

---

## 9 - Independent Work (March 4)

*   No new lecture or new material.

---

## 10 - Presentations and Multivariate Analysis techniques (March 6)

*   In the morning we will have the presentations from the articles chosen.
    *   The class will be split in half, with one session being chaired by Jason and the other session chaired by Preet
    *   The sessions will be held at NBB 2.1.I.156 and NBB 2.2.I.158, and room in which each group presents will be updated on the online spreadsheet for the assignment, that can be found in Absalon.
    *   Links to some to some of the previous presentations ([2016](../../2016/classes/#10-oral-presentations-in-class-non-parametric-tests), [2017](../../2017/classes/#10-presentations-and-multivariate-analysis-techniques), [2018](../../2018/StudentPresentations/), [2019](../../2019/StudentPresentations/), [2022](../../2022/StudentPresentations/), [2023](../../2023/StudentPresentations/), [2024](../../2024/StudentPresentations/))
    *   This years presentations can be found at [2025](./StudentPresentations.md)

**The Boosted Decision Trees**

*   [Lecture 10](Slides/Lecture10_MVA.pdf)
*   Data
    *   Exercise 1 ([training signal](data/BDT_signal_train.txt), [training background](data/BDT_background_train.txt), [testing signal](data/BDT_signal_test.txt), [testing background](data/BDT_background_test.txt))
    *   Exercise 2 (16 variable [file](data/BDT_16var.txt))
        *   The first column is the index, hence there are 17 'variables', but the index variable only for book keeping and has no impact on whether an event is signal or background.
        *   Every even row is the 'signal' and every odd row is the 'background'. Thus, there are two rows for each index in the first column: the first is the signal and the second is the background. [Format is odd, but I got it from a colleague].
    *   Here is the solution data sets separated into two files ([benign](data/benign_true.txt) and [malignant](data/malignant_true.txt)) for the last exercise of the lecture. Here is also the [(python) code](Exercises/Exam2_Problem_BDT_CheckSolutions_2016.py) that I used to establish the efficiency for all the submissions from all the students

---

## 11 - Statistical Hypothesis Tests and Auto-Correlation (March 11)

*   [Lecture slides](Slides/Lecture_AhlersKoskinen2025.pdf)
*   Files and some example code
    *   Data files in .FITS format: [eventmap1.fits](data/eventmap1.fits) and [truemap1.fits](data/truemap1.fits)
    *   Some example code (all in python): [C1_produce.py](Exercises/C1_produce.py) [C1_show.py](Exercises/C1_show.py) [KS_produce.py](Exercises/KS_produce.py) [KS_show.py](Exercises/KS_show.py) [maxLH_produce.py](Exercises/maxLH_produce.py) [maxLH_show.py](Exercises/maxLH_show.py) [powerspectrum.py](Exercises/powerspectrum.py) [twopoint.py](Exercises/twopoint.py) [Ylm.py](Exercises/Ylm.py)
*   **It is recommended (but not necessary)** to have [HEALPix software](https://healpix.jpl.nasa.gov) installed on your computer, or some other spherical surface pixelization software. There are options for C, C++, JAVA, Python, and I see some for MATLAB too. You will be expected to draw plots/graphs using spherical projections, e.g. mollweide maps.

---

## 12 - Work on Project (March 13)

*   No new lecture or new material.

---

## 13 - Work on Project (March 18)

*   No new lecture or new material.

---

## 14 - Nested Sampling, Bayesian Inference, and MultiNest (March 20)

*   [Lecture 13](Slides/Lecture13_MultiNest.pdf)
*   External packages for conducting nested sampling, e.g. MultiNest, are necessary and some python options are:
    *   nestle ([http://kbarbary.github.io/nestle/](http://kbarbary.github.io/nestle/))
    *   UltraNest ([https://johannesbuchner.github.io/UltraNest/index.html](https://johannesbuchner.github.io/UltraNest/index.html))
    *   Dynesty ([https://dynesty.readthedocs.io/en/stable/index.html](https://dynesty.readthedocs.io/en/stable/index.html))
*   Very good articles that are easy to read
    *   Excellent and readable paper by developer John Skilling on nested sampling ([http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf](http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf))
        *   **Read up until** the section "The Density of States"
    *   MultiNest academic papers
        *   [http://arxiv.org/abs/0809.3437](http://arxiv.org/abs/0809.3437)
        *   [http://arxiv.org/abs/1306.2144](http://arxiv.org/abs/1306.2144)

---

## 15 - Course Review, Non-Parametric Tests Lecture slides, Brief p-value slides (March 25)

*   [Review and recap](Slides/Lecture_Review.pdf) of a few topics covered in the course
*   [2016 Exam Solutions](Slides/AMAS_2016_Exam_solutions.pdf)
*   No solutions will be posted for the 2017 exam

*   [Non-parameteric tests slides](Slides/Lecture15_Nonparameteric.pdf) (EXTRA)
    *   Kolmogorov-Smirnov, Anderson-Darling, and Mann-Whitney U tests
    *   *Won't be be covered in class*
    *   Topics include things that may be useful for research
*   [P-Value slides](Slides/Lecture_PValue.pdf)
    *   Some extra material about p-values
    *   [PVals1_1.txt](data/PVals1_1.txt) [PVals1_2.txt](data/PVals1_2.txt)
    *   *Won't be be covered in class*

Extra Projects of a more difficult nature, for those who want something more challenging.

*   [Parameter Goodness-of-fit](Slides/ProblemFromMIT.pdf) (PG) in Global physics fits
