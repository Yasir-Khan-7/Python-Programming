# short hand if else in python
# it is used when we have simple logic in complex it is not prefered

a = 95
b = 67

print('hello') if a > b else "bye bye"

print("A") if a > b else print("=") if a == b else print("B")

# u can write expression aswell
c = 8 if a > b else 0
print(c)

# enumerated function ( built in ) that allows you to loop over a sequence ( list ,tuples or string) and get its index and value at the same time
# it return tuple and when index , mark is used then the tuple is unpacked
# u can also give starting index if u want by default it starts from 0
marks = [25, 43, 56, 7, 89, 76, 45]

for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print("yasir is amazing")

# virtual environment --> is a tool that isolates specific python environments on a single machines allowing you to work
# on different project with different dependencies and pakages without conflict this useful when working on projects with
# conflicting version of dependencies and pakages

# create virtual environment

#  python -m venv myenv   use this terminal to create your virtual environment

# acticate your Environment

# source myenv/bin/activate (linux/MACOS)
# .\venv\Scripts\activate.bat(windows using CMD)
# .\venv\Scripts\activate.ps1(windows using powershell)

# deacticate your Environment

# deeactivate write this to deactivate

# command = 'pip freeze' it gives you all the list of dependencies thatare istalled in your environment

# echo "X">main.py use to create a python file with X written in it

# pip freeze > requirements.txt  it will create a txt file that contain all dependencies
# if you want to send the dependencies file to your friend who is collaborating with you


# pip install -r requirements.txt  this command will install the dependencies present in txt file


# import is loading code from a python module into current script ,allow you to use the functions and variables
# into your current script as well as additional module that the import module may depend on
import math
print(math.sqrt(9))




# using from keyword when you want to import only specific function
from math import sqrt, pi
result = sqrt(16) * pi  # so u use directly the specific function

# using  'as' keyword it is used when u want to make the name short
import math as m
res = m.factorial(6)
print(res)


#using 'dir' it helps you to see all the functions that were imported
import math 
print(dir(math))

#import from other files 
from day7 import dummy
dummy()
