# AI-Lab-1
Designing fractal designs through a program and using AI and making a usable fractal design.
The tools used have been provided below:
BARNSLEY FERN PROGRAM — LIBRARIES & TOOLS USED
================================================

PYTHON VERSION
--------------
Python 3.10+ (uses the `int | None` type hint syntax introduced in 3.10;
for older Python versions, replace with `Optional[int]` from typing)

THIRD-PARTY LIBRARIES
----------------------
1. numpy
   - Purpose: Fast numerical array handling.
   - Used for: pre-allocating coordinate arrays, generating the random
     numbers that select which IFS transformation to apply, and vectorized
     math operations (min/max, normalization).
   - Install: pip install numpy

2. matplotlib
   - Purpose: Plotting and image rendering.
   - Used for: scatter-plotting the generated fern points, applying the
     custom colour gradient, styling the figure (background colour, title,
     removing axes), and saving the final PNG file.
   - Install: pip install matplotlib
   - Submodules used:
       - matplotlib.pyplot   (figure/axes creation, scatter plot, saving)
       - matplotlib.colors   (LinearSegmentedColormap for the custom
                               green colour gradient)

STANDARD LIBRARY MODULES
--------------------------
None required beyond built-ins used implicitly by the above (no explicit
`import os`, `import sys`, etc. are used in this script).

OTHER TOOLS (NOT PYTHON LIBRARIES)
------------------------------------
- pip — Python package manager, used to install numpy and matplotlib if
  not already available.
- A Python interpreter / environment to run the script (e.g. local
  Python install, virtual environment, Jupyter Notebook, or Google Colab).

QUICK INSTALL COMMAND
------------------------
pip install numpy matplotlib

FILE PRODUCED BY THE PROGRAM
------------------------------
- barnsley_fern.png (the rendered, colour-shaded fern image)
