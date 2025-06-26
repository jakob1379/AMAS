summary of the project.

The Structure

 • Source (AdvancedMethodsInAppliedStatistics2025/): This directory contains all the original course materials, including the main AMAS.html file, lecture PDFs, exercises,
   and data.
 • Destination (AMAS2025/): This is the root of a new MkDocs website. The source files for the website pages are located in AMAS2025/docs/.

The Task at Hand

The goal is to migrate the course content from the source directory (AdvancedMethodsInAppliedStatistics2025) into the new MkDocs site structure in the destination
directory (AMAS2025).

We are tackling this class by class:

 1 For each class session in Teaching/AdvancedMethodsInAppliedStatistics2025/AMAS.html, we create a corresponding index.md file under AMAS2025/docs/.
 2 We convert the relevant HTML content to Markdown.
 3 We adjust the links in the new Markdown files to point back to the original resources in the AdvancedMethodsInAppliedStatistics2025 directory using relative paths.
 4 We remove the migrated content from the original AMAS.html file.
