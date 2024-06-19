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
