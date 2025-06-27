# Advanced Methods in Applied Statistics 2025

[![Documentation Status](https://readthedocs.org/projects/amas2025/badge/?version=latest)](https://amas2025.readthedocs.io/en/latest/?badge=latest)

This repository contains the source materials for the AMAS2025 course website, built with MkDocs.

**Find the live page here: [https://amas2025.readthedocs.io/en/latest/](https://amas2025.readthedocs.io/en/latest/)**

## Course Overview

This course provides a practical introduction to advanced statistical methods used in modern scientific research. While students may use their preferred programming language for assignments, demonstrations and examples will primarily be in Python, using scientific packages like `SciPy`, `NumPy`, etc.

Key topics covered in the course include:

*   Multivariate analysis (MVA) techniques including Boosted Decision Trees (BDTs)
*   The MultiNest bayesian inference tool
*   Basis splines
*   Markov Chain Monte Carlo
*   Likelihood minimization techniques
*   Spherical surface isotropy

## Building the Website Locally

To build and view the site on your local machine, you will need Python and `pip`. It is recommended to work within a virtual environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jakob1379/AMAS2025.git
    cd AMAS2025
    ```

2.  **Install dependencies:**
    The site requires `mkdocs` and the `material` theme.
    ```bash
    #using uv
    uv sync
    
    # using pip
    pip install .
    ```

3.  **Serve the website:**
    Run the following command from the root of the repository:
    ```bash
    mkdocs serve -o
    ```
    This will start a local development server. You can view the website by navigating to `http://127.0.0.1:8000`. The site will automatically reload when you make changes to the source files.

4.  **(Optional) Build static files:**
    To generate the static HTML files for the site, run:
    ```bash
    mkdocs build
    ```
    The complete site will be generated in a new directory named `site/`.
