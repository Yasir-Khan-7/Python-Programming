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


# default argument --> it is called optional parameters and should come after the required parameter
def increment(number, by=1):  # by=1 is called default argument , you donot pass in calling and it comes after the required parameter
    return number + by


increment(2)

# *args is used to pull multiple number of arguments -->pass variable number of argument to function


def multiply(*number):  # so u can pull multiple arguments and it will be pakaged as tupples
    total = 1
    for number in number:
        total = total * number

    return total


multiply(2, 3, 4, 5)

# use of **args this will pull key  value pair argument and pakage as dictionary


def save_user(**user):
    print(user)  # will print the key value pairs in dictionary form


save_user(id=1, name='yasir', age=22)


# scope of function
# local and global variables

def fun():
    message = "hello"  # local variable of function


print(message)  # it will give error as the message has only scope inside function

message = 'a'  # global variable


def fun():
    message = "b"  # local variable of function


print(message)  # it will give 'a' as the message is outside the function
# and it cannot be overide in function as scope of that variable is inside

# use of global keyword
essage = 'a'


def fun():
    global message
    message = "b"  # it is now global variable


print(message)  # it will print "b" because of global variable

# fizzbuzz algo


def fizzbuzz(input):
    if (input % 3 == 0 & input % 5 == 0):
        return "FIZZ BUZZ"
    elif (input % 3 == 0):
        return "FIZZ"
    elif (input % 5 == 0):
        return "BUZZ"
    else:
        return input


print(fizzbuzz(5))

# classes OOP concepts

# if you want to leave something empty use 'pass' so that python will understand u want to use it later


class employee:
    pass


# class is basically a blue print of creating instances
#  emp_1 , emp_2 are both instances of class and are unique
emp_1 = employee()
emp_2 = employee()
print(emp_1)
print(emp_2)

# creating attributes manually
"""
emp_1.first = 'Yasir'
emp_1.last = "khan"
emp_1.email = 'Yasir.khan@gmail.com'
emp_1.pay = 1500

emp_2.first = 'Sharjeel'# it is instance attribute
emp_2.last = "khan"
emp_2.email = 'Sharjeel.khan@gmail.com'
emp_2.pay = 1500

print(emp_1.email)
print(emp_2.email)

"""
# now to avoid this use __init__ method which is initializer whenever the object is created the init method is initialized (just like constructor in java OOP)
# __init__ method takes self as first parameter and followed by the parameter you pass

# note in class we have attributes and methods
# note 'self' is important while creating methods


class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"." + last + "@company.com"
        self.pay = pay

    def Fullname(self):
        return f"{self.first} {self.last}"


emp_3 = employee('ahmed', 'khan', 3000)
emp_4 = employee('faizan', 'ahmed', 5000)
print(emp_3.email)
print(emp_4.email)

print(emp_4.Fullname())


# the above code we created instance variable --> by using the self keyword
# instance variable are unique for every instance
# while class variable are common to every instance--> shared among all employees
# creating class variables that can be accessed by class itself and aswell as with the object of the class
class employee:
    raise_amount = 1.04
    num_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"." + last + "@company.com"
        self.pay = pay
        employee.num_emp = employee.num_emp+1

    def Fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = employee('Yasir', 'khan', 4000)
emp2 = employee('ahmed', 'khan', 2900)
print(employee.num_emp)  # it will be changed whenever new object is created
emp1.apply_raise()
# employee.apply_raise(emp1) #the  emp1.apply_raise() converted to this both are same at run time it converts
print(emp1.pay)  # raise is applied as it common among all employees

# Note instance attribute get preference over class attribute during assignment and retrieval


class employee:
    language = 'py'
    salary = 12000


emp5 = employee()
emp6 = employee()

emp5.language = 'JAVASCRPT'
# here in language will be 'Javascript' because of prefenrce of instance attribute
print(emp5.language, emp5.salary)


# Practice set
# problem #1 create programmer class  and stores information of programmers working at microsoft
class programmer:
    company = 'Microsoft'

    def __init__(self, position, salary, name):

        self.position = position
        self.slary = salary
        self.name = name


p1 = programmer('Python developer', 14000, 'yasir')
p2 = programmer('Java Developer', 12000, 'suffian')

# problem #2 create Calculator class that calculate , square,cube and square root of a number
# The ** operator is a convenient way to perform power calculations in Python.
# it is base ** exponent


class calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return f"square is {self.number*self.number}"

    def cube(self):
        return f"cube is {self.number*self.number*self.number}"

    def squareroot(self):
        return f"square root is {self.number**1/2}"


num = calculator(4)

print(num.square())
print(num.cube())
print(num.squareroot())

# 3 now create class attribute a and set value to a and now create instance attirubute a and check it change class atribute or not?


class demo:
    a = 4


obj1 = demo()
print(obj1.a)  # before instance attribute the value of  a=4 for child
obj1.a = 3
# once instance attribute with same name is created then it will print a=3
print(obj1.a)

# 4 add static method to the problem #2 that greets


class calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return f"square is {self.number*self.number}"

    def cube(self):
        return f"cube is {self.number*self.number*self.number}"

    def squareroot(self):
        return f"square root is {self.number**1/2}"

    @staticmethod
    def hello():
        print("hello there!")


num = calculator(4)
num.hello()

# 5 Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint
class Train:
    def __init__(self, trainno):
        self.traino = trainno

    def Book_ticket(self, fro, to):
        print(f"train ticket booked of {self.traino} from {fro} to {to}")

    def get_status(self):
        print(f"The train no {self.traino} is running on time")

    def get_fare(self, fro, to):
        print(f" ticket fare in train no: {self.traino} from {
              fro} to {to} is {randint(300, 5000)}")


t = Train(45678)
t.Book_ticket("peshawar", 'karachi')
t.get_fare("islamabad","lahore")
# 6 can you change the 'self' parameter = yes u can write anything but self is conventional so easy to understand
