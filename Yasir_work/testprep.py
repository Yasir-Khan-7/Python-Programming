# string are immutable
# anything u enclose in double or single quote is called string
name = 'yasir'
friend = 'sharjeel'
# when u want to add double quote
print("""hello 
    jani kaisay ho
    """)
# indexing in string
print(name[0])

# looping through string
for i in name:
    print(i)
print(len(name))

# methods in string

# len()
print(len(name))
# touppercase()
print(name.upper())  # it creates a copy of it as string is immutable
# now lower method
print(name.lower())

# strip method strip from all side
d = 'hello!!!'
print(d.strip("!"))

# rstrip -->rstrip  only from end
d = "!!!!hello!!!!"
print(d.rstrip("!"))

# replace()
name = 'john'
newname = 'sharjeel'
print(name.replace(name, newname))
# split method it splits the text
name = 'yasir is sharjeel'
print(name.split(" "))

# capitalize method it capatalize the first letter

print(name.capitalize())


print('hello jani')
# IT Center the text
print(name.center(100))
print(name.endswith("@"))
print(name.endswith("ir", 0, 5))


# endswith() returns true and false for checking
print(name.endswith("@"))
# now see this
print(name.endswith('to', 2, 8))  # ending index will be checked

# find() method give index else if not found give -1

print(name.find("is"))

# index() method is same like but gives exception on if not found
# print(name.index("jjgh"))

# isalnum() give true if entire string only is Either CAPITAL A-Z or Small a-z or 0-9
str = 'HELLO'
str2 = '096'
print(str.isalnum())
print(str2.isalnum())

# isalpha give true if entire string only is Either CAPITAL A-Z or Small a-z
print(str.isalpha())
print(str2.isalpha())  # false because number not in isalpha

# islower() checks whether all string are lower character and gives true if present otherwise false
print(str.islower())  # false because of capital

# isupper() checks whether all string are upper character and gives true if present otherwise false
print(str.isupper())  # true because of upper

# isprintable -- gives true if characters are printable means it doesnot include special characters
str3 = 'hello world brother'
str4 = "hello i am special \n ok"
print(str3.isprintable())
print(str4.isprintable())  # false because of \n it is not printable character

# ispace() only gives true for only empty space
empty = "   "
print(empty.isspace())

# istitle() search about it
# title() search about it

name1 = 'he is good boy'
# startswith() if you string starts with gives true otherwise false
print(name1.startswith("he"))


# loops when you want to do something repeatedly a task or anything
for number in range(5):
    print("attempt:", number+1, (number+1)*".")
# note in python if you multiply a number with string so string is repeated by that number

# for with else
success = False
for number in range(3):
    print("attempt")
    if success:
        print('successful')
        break

else:
    print("attempted 3 times and fails")

# loop in loops

for x in range(3):
    for y in range(3):
        print(f"({x},{y})")

# range function
# range is of complex type
# while string int are primitive type
# range is iterable plus note: string are also iterable
print(type(range(4)))

# quiz print even numbers
count = 0
for x in range(1, 10):
    if (x % 2 == 0):
        print(x)
        count = count+1

print(f"we have {count} even number")

# another way
count = 0
for x in range(2, 10, 2):
    print(x)
    count = count+1
print(f"we have {count} even number")

# while loop will execute as long as the condition is true
name = ''
while len(name) == 0:
    name = input("enter you name please:")

print(f"your name is {name}")

# use while loop to print number upto certain condition
x = int(input("enter a number"))

while x < 5:

    print(x)
    x = x+1

# quiz

age = ""
while len(age) == 0:
    age = input("Enter your age")
print("your age is ", age)

# functions


def fun1():
    print("welcome to test prep")


fun1()


# parameter is input you define for your function
# while the argument is value you for given parameter

def greet(first_name, Last_name):  # parameter when defining function
    print(f" HI {first_name} {Last_name}")


greet("yasir", "khan")  # arguments while calling function


# types of functions
# 1-perform a task
# 2- return a value

# 1
def greet(name):
    print(f"helllo my name is  {name}")


greet("yasir")
# this will return none aswell because in python by default all function return none value
print(greet("yasir"))
# none is object that represent absence of value

# 2


def get_greeting(name):
    return f"HI {name}"


message = get_greeting("yasir")


# keyword argument --> to make your code more readable and understandable
def increment(number, by):
    return number + by


# for better understanding u can add keyword as 'number' =2 to know what actually your argument is
increment(number=2, by=1)
