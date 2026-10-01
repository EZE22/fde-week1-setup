# hello_fde.py
# My first script for the FDE program.
# Lines that start with # are comments. Python skips them.
# They explain what the code does so people can read it later.

# STEP A: Load a tool that comes built into Python.
# "datetime" knows about dates. We borrow its "date" feature.
from datetime import date

# STEP B: Store your name in a variable.
# A variable is a labeled box that holds a value.
# CHANGE "Your Name" to your real name. Keep the quotation marks.
my_name = "Adam Ingram"

# STEP C: Define a function.
# A function is a reusable set of instructions with a name.
# This one is called add_numbers. It takes two numbers, a and b,
# and "returns" (hands back) their sum.
def add_numbers(a, b):
    return a + b

# STEP D: Get today's date from the computer's clock.
today = date.today()

# STEP E: Print your name and the date to the screen.
print("Name:", my_name)
print("Date:", today)

# STEP F: Use the function. We give it 3 and 4,
# store the answer in a variable called result, and print it.
result = add_numbers(3, 4)
print("3 + 4 =", result)
