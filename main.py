# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions from the module mod using any two numbers.
# Import the module

import mod
# Call the functions from the module
mod.psum(5, 3)  # Prints the sum of 5 and 3
mod.pmultiply(4, 2)  # Prints the product of 4 and 2

# 7.4.3 In main.py, also import Python's built in module platform. Then list the functions and variables in the platform module using the dir() function.

# Import the platform module
import platform

# List functions and variables in platform using dir()
print("\nFunctions and variables in platform module:")
print(dir(platform))
