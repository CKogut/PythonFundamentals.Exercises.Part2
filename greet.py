# Define a function called *greet* that meets the following criteria: 
#   * Takes an argument called *name*.
#   * Prints a greeting using the *name* parameter.
# Define another function called *name_input* that meets the following criteria:
#   * Takes no arguments.
#   * Prints a message to the screen requesting the user to provide a name.
#  * Returns a string with the value equals to that of the provided name.
# Using these two functions, prompt the user for a name and print it to the screen.
# Each function must have an appropriate docstring.

"""Prints a greeting"""
def greet(name):
    print("Hello there, " + name)

"""Prompts user for name"""
def name_input():
   return input("Enter name: ")
   
"""Pass name_input to greet"""
greet(name_input())


