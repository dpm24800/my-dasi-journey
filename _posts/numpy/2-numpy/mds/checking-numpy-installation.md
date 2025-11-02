To check if NumPy is installed using the Command Prompt (CMD), you can use one of the following methods: 

1\. Using `pip show numpy`: 

This command directly queries `pip`, the Python package installer, for information about the NumPy package. 

Code

```
python -m pip show numpy
```

Code copied!

If NumPy is installed, this command will display details such as the name, version, summary, and location of the installed NumPy package. If it is not installed, it will indicate that the package was not found. 

2\. Using `pip list` and filtering: 

This method lists all installed Python packages and then filters the output to find "numpy." 

Code

```
pip list | findstr /i "numpy"
```

Code copied!

If NumPy is installed, this command will display the line containing "numpy" and its version number. If it is not installed, no output related to NumPy will be shown. 

3\. Importing in Python interactive shell: 

This method involves launching a Python interactive session and attempting to import NumPy. 

Code

```
python
```

Once in the Python interactive shell, type: 

Python

```
import numpy as np
```

If NumPy is installed, no error will be displayed, and you can then check the version using `print(np.__version__)`. If NumPy is not found, an `ImportError` will be raised, indicating that the module is not installed. To exit the interactive shell, type `exit()`.