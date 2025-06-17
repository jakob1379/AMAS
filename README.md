# AMAS2025
Probably the best course on applied statistics ever known. Do the exercises one by one and structure your code as a package for maximum gain and usability in the future!

# Usage

This project uses Sphinx to generate documentation for a Python project. Follow the instructions below to set up the project and build the HTML documentation.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.6 or higher
- Make

## Setup

1. Clone the repository and navigate to the project directory.
2. Run `make install` to create a Python virtual environment and install the necessary dependencies from the `requirements.txt` file.
3. Activate the virtual environment:
   - On Linux or macOS, run `source venv/bin/activate`
   - On Windows, run `venv\Scripts\activate`

## Building the Documentation

To build the HTML documentation, simply run the following command:

 `make html`

This will generate the HTML files in the `build/html` directory. Open the `index.html` file in a web browser to view the generated documentation.

## Deactivating the Virtual Environment

When you're done working with the project, you can deactivate the virtual environment:

- On Linux or macOS, run `deactivate`
- On Windows, run `deactivate.bat`

