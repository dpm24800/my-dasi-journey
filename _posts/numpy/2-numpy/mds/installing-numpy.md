To install NumPy using the Command Prompt (CMD) in Windows, follow these steps: 
-   **Open Command Prompt:** Press the Windows key, type "CMD", and press Enter to open the Command Prompt.
-   **Install NumPy:** Type the following command and press Enter:

Code

        pip install numpy

Code copied!

Alternatively, if you have multiple Python versions or encounter issues, you can use: 

Code

        py -m pip install numpy

Code copied!

-   **Verify Installation (Optional):** After the installation completes, you can verify it by opening a Python interpreter in the Command Prompt and attempting to import NumPy: 

Code

        python

Code copied!

Then, within the Python interpreter: 

Python

        import numpy as np    print(np.__version__)

Code copied!

If no errors occur and the NumPy version is displayed, the installation was successful. Exit the interpreter by typing `exit()` and pressing Enter.

