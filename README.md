<p align="center">
  <img src=".github/assets/mcmc-chain.svg" width="960" alt="A Metropolis-Hastings chain starts in the tail of a correlated two-dimensional posterior and random-walks into its core; rejected proposals flash and vanish while every draw stacks onto the marginal histograms of theta one and theta two, which grow towards the true marginal curves">
</p>

# Advanced Methods in Applied Statistics

Source for the course website of Advanced Methods in Applied Statistics (AMAS)
at the University of Copenhagen, built with MkDocs and the Material theme.

**Live site: [jakob1379.github.io/AMAS/latest](https://jakob1379.github.io/AMAS/latest/)**

The site is versioned with [mike](https://github.com/jimporter/mike): each
course year from 2016 to 2025 is published as its own version, and `latest`
points to 2025.

## The course

A practical introduction to advanced statistical methods used in modern
scientific research. Students may use any programming language for
assignments; demonstrations and examples are mainly in Python with scientific
packages such as `SciPy` and `NumPy`.

Topics include:

- Multivariate analysis (MVA) techniques, including Boosted Decision Trees (BDTs)
- The MultiNest Bayesian inference tool
- Basis splines
- Markov Chain Monte Carlo
- Likelihood minimization techniques
- Spherical surface isotropy

## What is in this repository

| Path                         | Contents                                                            |
| ---------------------------- | ------------------------------------------------------------------- |
| `docs/index.md`              | Course home: educators, schedule, evaluation, syllabus              |
| `docs/classes.md`            | Notes and links for each class                                      |
| `docs/Slides/`               | Lecture slides, course information and past exams (PDF)             |
| `docs/Exercises/`            | Example solutions as Python scripts and Jupyter notebooks           |
| `docs/data/`                 | Data files used in the exercises                                    |
| `docs/StudentPresentations/` | Student journal-article presentations and write-ups                 |
| `overrides/`, `styles/`      | Theme template override and custom CSS                              |
| `mkdocs.yml`                 | Site configuration                                                  |

## Build the site locally

You need Python 3.13 or newer. Working inside a virtual environment is
recommended.

1. **Clone the repository**

   ```bash
   git clone https://github.com/jakob1379/AMAS.git
   cd AMAS
   ```

2. **Install dependencies** (`mkdocs`, `mkdocs-material` and plugins)

   ```bash
   # using uv
   uv sync

   # using pip
   pip install .
   ```

3. **Serve the site**

   ```bash
   mkdocs serve -o
   ```

   This starts a development server at `http://127.0.0.1:8000` and reloads
   the page when you change the source files.

4. **Build static files** (optional)

   ```bash
   mkdocs build
   ```

   The complete site is written to `site/`.

## Publish a course year

The `deploy` task in `pyproject.toml` runs `mike deploy`, pushes the result
and moves the `latest` alias to the given version:

```bash
uv run poe deploy --version 2025
```
