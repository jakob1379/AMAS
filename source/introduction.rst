Advanced Methods in Applied Statistics 2023
===========================================

.. image:: ./_static/introduction_files/DJK.jpeg

.. note::
  | Lecturer: D. Jason Koskinen
  | Email: koskinen (at) nbi.ku.dk
  | TA: "Juno" Chun Lung Chan
  | Email: chun.lung.chan (at) nbi.ku.dk

Basic Information
-----------------

* Block 3 - Timetable A of the 2023 `academic calendar <http://www.science.ku.dk/english/student-life/studying-at-the-faculty/academic-calendar/>`__

  * Tuesday 08:00 - 12:00 and Thurs 08:00- 12:00 & 13:00 - 17:00
  * Actual

    * 08:45 - 09:00 Q&A or discussion with Jason
    * **09:00** lecture on new material (not 09:05 or 09:15)
    * On Thursday there will often be new material starting at 13:00
    * On Thursday it is very unlikely that any new material, lectures, or review will happen after 16:00.

  * Class Location: øv - bib 4-0-17, Universitetsparken 1-3, DIKU
  * Official schedule (`link <https://skema.ku.dk/tt/tt.asp?SDB=KU2223&language=DK&folder=Reporting&style=individual&type=module&idtype=id&id=114333&weeks=28-38&days=1-5&periods=1-68&width=0&height=0&template=SWSCUST2+module+individual>`__)

 * Classes will be composed of ~20-30% lecture and demonstrations followed by exercise
 * While assignments, projects, and exercises can be done in the programming language of the students choice, the examples and demonstrations will be mainly in Python and/or scientific packages thereof, i.e. SciPy, NumPy, etc.
 * Required text or textbooks: None
 * 2016 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2016/AdvancedMethodsAppliedStatistics2016.html>`__
 * 2017 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/AdvancedMethodsAppliedStatistics2017.html>`__
 * 2018 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2018/AdvancedMethodsAppliedStatistics2018.html>`__
 * 2019 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2019/AdvancedMethodsAppliedStatistics2019.html>`__
 * 2020 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2020/AdvancedMethodsAppliedStatistics2020.html>`__
 * 2021 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2021/AMAS.html>`__
 * 2022 Advanced Methods in Applied Statistics `webpage <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2022/AMAS.html>`__
 * It is recommended, but not required, to have taken an introdcutory course on statistics, e.g. "Applied Statistics - From data to results" which can be found `here <http://www.nbi.dk/%7Epetersen/Teaching/AppliedStatistics2022.html>`__

Evaluation
==========

The presentation, the problems sets, and the project will all be
submitted and assigned from Absalon. So check Absalon for instructions
and due dates. The final exam is handled by the eksamen webpage.

 * Presentation and 1-2 page summary (10%)
 * Graded problem sets (20%)
 * Project (30%)

   * You may start working on **this right now!!**

 * Final exam (40%)

   * 28 hour take home exam starting on the morning of March 30 and ending on afternoon of March 31
   * The exam will be similar to problem sets 2 and 3

     * A handful of more intensive questions as opposed to numerous short questions
     * The exam will contain problems from any portion of the course material, excluding guest lectures unless otherwise noted.

   * `Here <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2020/ExtraProblems.pdf>`__ are two extra practice problems and the exams for `2016 <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2020/Exam_2016.pdf>`__ and `2017 <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2020/Exam_2017.pdf>`__

Course Syllabus
===============

The course is very likely to change once we begin, and future lectures
listed below serve as an outline. Even so, we are very likely to cover
the following topics which may require additional software support:

-  Multivariate analysis (MVA) techniques including Boosted Decision
   Trees (BDTs)
-  The MultiNest bayesian inference tool
-  Basis splines
-  Markov Chain Monte Carlo
-  Likelihood minimization techniques
-  Spherical surface pixealization and isotropy (HealPix)

.. note:: Class notes will be posted here on this webpage as they become available.

Optional Software Help Session (Jan. 27)
----------------------------------------

-  13:00-16:00 in room 4-0-17 at DIKU
-  Optional session with the Teaching Assistant ( "Juno" Chung Lung Chan) for any students who may need assistance with their computer software setup.
-  Get a preview with the course and some software tools to install.


Class 1 - Start (Feb. 7)
------------------------

 * `Course Information <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/CourseInformation.pdf>`__
 * Chi-square
 * Code chi-square
 * Data for exercise 1 (`FranksNumbers.txt <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2018/data/FranksNumbers.txt>`__)
 * Review of 'basic' statistics
 * `Lecture 1 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture1_Basics_ChiSquare.pdf>`__

   * Jean-Loup's (2019 TA) `python 3 code as a Jupyter notebook <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture1_Variance_Py3.ipynb>`__ for exercise 1
   * Tania's (2021 TA) `python 3 code as a Jupyter notebook <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/class1_exercise1.ipynb>`__ for exercise 1

 * Start reading paper about how well Gaussian statistics compares to a wide selection of scientific measurements

   * "Not Normal: the uncertainties of scientific measurements" link at `arXiv <https://arxiv.org/abs/1612.00778>`__ or `DOI <http://rsos.royalsocietypublishing.org/content/4/1/160600>`__
   * We will be discussing the paper in the next class, i.e. on Thursday


Class 2 - Monte Carlo Simulation & Least Squares (Feb. 9)
---------------------------------------------------------

 * `Lecture 2 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture2_MC_LeastSquares.pdf>`__
 * Monte Carlo (reminder that lecture starts at 09:00)
 * Code for `area of the circle <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture2_CircleArea.py>`__. Note that the code is provided for illustrative purposes, and not as a piece of code that students are expected to be able to execute without modification.
 * `Example code <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture2_CircleArea_Py3.ipynb>`__ from Jean-Loup (2019 TA) in a Jupyter notebook
 * `Example code <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/class2_exercises.ipynb>`__ from Tania (2021 TA) in a Jupyter notebook
 * From the "Not Normal: the uncertainties of scientific measurements" `paper <https://arxiv.org/abs/1612.00778>`__:

   * For the ambitious, create a 'toy monte carlo' of the sample and pair distributions for the nuclear physics data in Sec. 2.A. For simplicity assume that all the 'quantities' are gaussian distributed.
   * Write functions where you can produce multiple gaussian distributions to sample from and generate a sample of "12380 measurements, 1437 quantities, 66677 pairs".
   * Produce the z-distribution (using Eq. 4) plot for just your toy Monte Carlo and see if it matches a gaussian, exponential, student-t distribution, etc...

 * Discussion of "Not Normal: the uncertainties of scientific measurements" (`arXiv <https://arxiv.org/abs/1612.00778>`__ or `DOI <http://rsos.royalsocietypublishing.org/content/4/1/160600>`__)
 * Included here are some `prompt questions <https://alumni-my.sharepoint.com/:w:/g/personal/xdn365_ku_dk/EQqplhQcBi5AgoDX5K92HfQBQon-bJvNZmn_SQzxvEUshQ?e=VTH9AJ>`__ to accompany discussion and understanding of the paper

 * Least Squares (optional)
 * Some useful links
 
   * `Covariance Matrix (wiki) <https://en.wikipedia.org/wiki/Covariance_matrix>`__
   * `In-Depth (but still brief) least-squares write-up <http://stat.ethz.ch/%7Egeer/bsa199_o.pdf>`__


Class 3 - Introduction to Likelihoods and Numerical Minimizers (Feb. 14)
------------------------------------------------------------------------

 * `Lecture 3 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture3_General_Likelihood.pdf>`__
 * Maximum likelihood method
 * Gradient descent and minimizers
 * Example code for `exercise 1 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/class3_exercise1.ipynb>`__ and `exercise 2-3 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/class3_exercises2-3.ipynb>`__ from Tania, `exercise 1 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture3_Exercise1.ipynb>`__ and `exercises 2 & 3 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture3_Exercises2-3.ipynb>`__ from Jean-Loup (TA in 2018 & 2019),  `Niccolo <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture3_likelihood_niccolo.py>`__ (TA in 2017), some from `Jason <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture3_MLE_Cowan_clean.py>`__ (course lecturer)


Class 4 - Intro. to Bayesian Statistics & Splines (Feb. 16)
-----------------------------------------------------------

 * `Lecture 4 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture4_Bayes.pdf>`__ on Simple Bayesian statistics 
 * Using priors, posteriors, and likelihoods
 * Example `code <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture4_Bayes_1.py>`__ for exercises from Jason, and `example code <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/class4_bayes.ipynb>`__ from Tania 
 * `Lecture 4.5 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture4.5_Splines.pdf>`__
 * Splines
 * Data files for one of the exercises.

   * `Dust Logger data <https://www.nbi.dk/~koskinen/Teaching/data/DustLog_forClass.dat>`__
   * `Spline cubic data <https://www.nbi.dk/~koskinen/Teaching/data/SplineCubic.txt>`__
   * `Spline oscillation data <https://www.nbi.dk/~koskinen/Teaching/data/SplineOsc1.txt>`__

 * Interesting article about use of splines and penalty terms

   * `Penalized splines <https://arxiv.org/pdf/1301.2184v1.pdf>`__


Class 5 - Parameter Estimation and Confidence Intervals (Feb. 21)
-----------------------------------------------------------------

 * `Lecture 5 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture5_ConfidenceIntervals.pdf>`__ Confidence intervals
 * Numerical minimizers for best-fit values
 * `Data file <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/ParameterEstimation_Ex1.txt>`__ for exercise 1
 * `Data file <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/MLE_Variance_data.txt>`__ for exercise 3 (`extra data file <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/MLE_Variance_data_2.txt>`__)
 * Reminder: oral presentation and 1-2 page article reports will be due soon

   * `Article about Supernova <https://arxiv.org/abs/1701.02596>`__ first detection time. Look at the caption for the Supplementary Fig. 8


Class 6 - Markov Chain(s) (Feb. 23)
-----------------------------------

 * `Lecture 6 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture6_MCMC_Bayes.pdf>`__ Markov Chain Monte Carlo (MCMC)
 * Look for an external package for Markov Chain Monte Carlo (MCMC), e.g. emcee

   * Just like minimizers, syntax and options matter
   * Be familiar with your chosen MCMC package

 * Some example python code for the exercises (caveat emptor)

   * `Using emcee <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Lecture6_MCMC_Example1_Niccolo.py>`__, the solution is graciously provided by Niccolo Maffezzoli (2017 TA)


Class 7 - Hypothesis Testing (Feb. 28)
--------------------------------------

 * `Lecture 7 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture7_HypothesisTests.pdf>`__
 * Likelihood ratio
 * Data files for one of the exercises. Just use the first column in each file. The second column is unimportant.

   * `Data set 1 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/LLH_Ratio_2_data.txt>`__
   * `Data set 2 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/LLH_Ratio_2a_data.txt>`__


Class 8 - Independent work (March 2)
------------------------------------

 * No new lecture material.
 * Time to work on presentation and/or write-up.
 * Jason and Juno will be around (in some combination), from 8:30-15:30 in the classroom.


Class 9 - TBD (March 7)
-----------------------

 * Maybe something new, but if so the topic would not be part of an assignment or on the final exam.
 * Will likely be one of:

   * Independent work session
   * Topic about sub-threshold anomaly detection in binned data
   * Pre-recorded video (available on Absalon) with more content about p-values.


Class 10 - Presentations and Multivariate Analysis techniques (March 9)
-----------------------------------------------------------------------

 * In the morning we are likely to have the presentations from the articles chosen.

   * The class will be split in half, with one session being chaired by Jason and the other session chaired by Chun
   * Links to some to some of the previous presentations (`2016 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2016/Presentations_2016.html>`__, `2017 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/StudentPresentations2017.html>`__, `2018 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2018/StudentPresentations2018.html>`__, `2019 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2019/StudentPresentations2019.html>`__, `2022 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2022/StudentPresentations.html>`__)
   * This years presentations can be found at `2023 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/StudentPresentations2023.html>`__

The Boosted Decision Trees

 * `Lecture 10 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture10_MVA.pdf>`__
 * Data

   * Exercise 1 (`training signal <https://www.nbi.dk/~koskinen/Teaching/data/BDT_signal_train.txt>`__, `training background <https://www.nbi.dk/~koskinen/Teaching/data/BDT_background_train.txt>`__, `testing signal <https://www.nbi.dk/~koskinen/Teaching/data/BDT_signal_test.txt>`__, `testing background <https://www.nbi.dk/~koskinen/Teaching/data/BDT_background_test.txt>`__)
   * Exercise 2 (16 variable `file <https://www.nbi.dk/~koskinen/Teaching/data/BDT_16var.txt>`__)

     * The first column is the index, hence there are 17 'variables', but the index variable only for book keeping and has no impact on whether an event is signal or background.
     * Every even row is the 'signal' and every odd row is the 'background'. Thus, there are two rows for each index in the first column: the first is the signal and the second is the background. [Format is odd, but I got it from a colleague].

   * Here is the solution data sets separated into two files (`benign <https://www.nbi.dk/~koskinen/Teaching/data/benign_true.txt>`__ and `malignant <https://www.nbi.dk/~koskinen/Teaching/data/malignant_true.txt>`__) for the last exercise of the lecture. Here is also the `(python) code <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/Exam2_Problem_BDT_CheckSolutions_2016.py>`__ that I used to establish the efficiency for all the submissions from all the students


Kernel Density Estimator
------------------------

 * `KDE Lecture  Slides <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture_KDE.pdf>`__
 * On Absalon there is a video in the "Media Gallery" tab for a lecture on using Kernel Density Estimators. The slides will be slightly different than what is linked here, but the lecture content remains very similar and relevant.

Class 11 - Work on Project (March 14)
-------------------------------------

 * No new material.
 * Unfortunately neither Jason nor Juno will be availabe in person, but
   may be available via Slack or email.

Class 12 - Statistical Hypothesis Tests and Auto-Correlation (March 16)
-----------------------------------------------------------------------

 * `Lecture slides <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture_AhlersKoskinen2023.pdf>`__
 * Files and some example code
   
   * Data files in .FITS format: `eventmap1.fits <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/eventmap1.fits>`__  and `truemap1.fits <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/data/truemap1.fits>`__
   * Some example code (all in python): `C1_produce.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/C1_produce.py>`__ `C1_show.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/C1_show.py>`__ `KS_produce.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/KS_produce.py>`__ `KS_show.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/KS_show.py>`__ `maxLH_produce.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/maxLH_produce.py>`__ `maxLH_show.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/maxLH_show.py>`__ `powerspectrum.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/powerspectrum.py>`__ `twopoint.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/twopoint.py>`_ `Ylm.py <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Exercises/Ylm.py>`__ 

 * **It is recommended (but not necessary)** to have `HEALPix software <https://healpix.jpl.nasa.gov/>`__ installed on your computer, or some other spherical surface pixelization software. There are options for C, C++, JAVA, Python, and I see some for MATLAB too. You will be expected to draw plots/graphs using spherical projections, e.g. mollweide maps.

 * No afternoon session

Class 13 - Nested Sampling, Bayesian Inference, and MultiNest (March 21)
------------------------------------------------------------------------

 * `Lecture 13 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture13_MultiNest.pdf>`__
 * External packages for conducting nested sampling, e.g. MultiNest, are necessary and some python options are:

   * pymultinest (https://johannesbuchner.github.io/PyMultiNest/)
   * nestle (http://kbarbary.github.io/nestle/)
   * UltraNest (https://johannesbuchner.github.io/UltraNest/index.html)
   * SuperBayeS  (http://www.ft.uam.es/personal/rruiz/superbayes/?page=main.html)

 * Very good articles that are easy to read

   * Excellent and readable paper by developer John Skilling on nested sampling (http://www.inference.phy.cam.ac.uk/bayesys/nest.pdf)

     * **Read up until** the section "The Density of States"

   * MultiNest academic papers

     * http://arxiv.org/abs/0809.3437
     * http://arxiv.org/abs/1306.2144

Class 14 - Work on Project (no lecture or new material - March 23)
------------------------------------------------------------------
.. warning:: empty

Class 15 - Course Review**, and Non-Parametric Tests Lecture snippet (March 28)
-------------------------------------------------------------------------------

 * `Review and recap <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture_Review.pdf>`__  of a few topics covered in the course
 * `2016 Exam Solutions <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2016/AMAS_2016_Exam_solutions.pdf>`__
 * No solutions will be posted for the 2017
 * `Lecture 15 <https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2023/Lecture15_Nonparameteric.pdf>`__ (EXTRA)

   * Kolmogorov-Smirnov, Anderson-Darling, and Mann-Whitney U tests
   * *Won't be be covered in class*
   * Topics include things that may be useful for research

Extra Projects of a more difficult nature, for those who want something more challenging.

 * `Parameter Goodness-of-fit <http://www.nbi.dk/%7Ekoskinen/Teaching/AdvancedMethodsInAppliedStatistics2016/ProblemFromMIT.pdf>`__ (PG) in Global physics fits
