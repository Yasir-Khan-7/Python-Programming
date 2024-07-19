import math

#Note: & in Python

# The ‘&‘ symbol is a bitwise AND operator in Python, it is also known as a bitwise AND operator.
# It operates on the bitwise representation of integers.

# Note: The ‘and‘ keyword in Python is used in the logical operations. It is used to combine two logical statements, 
# it returns TRUE if both are correct and FALSE if any of the statements is wrong.

## Q1 write a program diivsible by 7 not multple of 5 from 2000 to 3200

lst =[]
for number in range(2000,3200):

    if number%7==0 and number%5!=1:
        lst.append(number)

print(lst)

## Q2 write a program to calculate its factorial
# # fact of 0 and 1 is always 1

def factorial(num):
    if num ==0 and 1:
        return 1
    else:
       return num*factorial(num-1)
res = factorial(5)
print(f"The factorial of {5} is: {res}")


## Q3 program 3 write a program that takes a number 
## and creates dictionary of all previous numbers key is its index and square is its  value

Dictionary={}
def dict_number(num):
    
    for  x in range(1,num):
     
        Dictionary[x] = x*x
        
dict_number(5)    
print(Dictionary)

## Q4 check for prime factors
lst2 = []
def Prime(num):
    for x in range(2,num):
        
        if  num%x==0:
            return False
        else:
            return True
       
res =Prime(13)
print(res)    

## Q5 check for palindrome

def palindrome(str):
        if str  == str[::-1]:

            print("String is palindrome")
         
        else:
            print("is not palindrome")
        
palindrome("yasir")

## Q6
# Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:


lst1 =[]
lst2 = []

for x in range(0,5):
    number = input(f"Enter  number:{x+1} ")
    lst1.append(number)
    lst2.append(number)
    tup = tuple(lst2)
    
print(lst1)
print(tup)

## Q6
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Stringbox:
    def __init__(self):
        self.str = " "

    def getString(self):
        self.str = input("Enter the String: ")
    def printString(self):
        print(self.str)
    
obj = Stringbox()
obj.getString()
obj.printString()



## Q7
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

def calculateQ(*args):
    print(args)
    new_lst = []
    C = 50
    H = 30 
    for x in args:
        print(x)
        Q = math.sqrt((2*C*x)/H)
        new_lst.append(str(int(round(Q))))
    return new_lst

res =calculateQ(23,24,33)
print(res)


## Q8 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.


def two_dimensional(num1,num2):
    twoD = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(num1):
        for y in range(num2):
         
            twoD[x][y] = x*y     
          
    print(twoD)
two_dimensional(3,3)  
    
    
## Q9 Write a program that accepts a comma separated sequence of words 
# as input and prints the words in a comma-separated sequence after sorting them alphabetically.

def Sorting_words():
    lst =[]
    for x in range(4):
        word = input("Enter word:  ")
        lst.append(word)
    lst.sort()
    return lst
        
    # return lst.sort()

print(Sorting_words())


## Q10
# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

user_input = input("Enter your desired statement: ")
lines =[]

while True:
    user_input = input("Please enter your desired string: ")
    if user_input:
        lines.append(user_input.upper())
    else: 
        break
print("your desired lines are: ",lines)

## Q11
# Write a program which accepts a sequence of comma separated
# 4 digit binary numbers as its input and then check whether 
# they are divisible by 5 or not. The numbers that are divisible 
# by 5 are to be printed in a comma separated sequence.

number = int(input("Enter 4 digit number: "))

if number%5==0:
    print(number)
else:
    print("number is not divisble by 5")


## Q12
# Write a program, which will find all such numbers between 1000 and 3000 
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
lst =[]
for x in range(1000,3001):
    if x%2==0:
        lst.append(x)
print(lst)

## Q13
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:

letter_and_digit = input("Enter letter and some digits: ")
letter = 0
digit = 0
for x in letter_and_digit:
    if x.isdigit():
        digit+=1
    elif x.isalpha():
        letter+=1
    else:
        print("not a letter or digit")
print("letter count is: ",letter)
print("digit count is: ",digit)

## Q14 create a function that counts the number of vowels in a string

def count_vowel(str):
    count =0
    lst = ['a','e','i','o','u']
    for x in str:
        if x in lst:
            count+=1
    return count
user_input = input("Enter your string: ").lower()       

res =count_vowel(user_input)
print(res)

## Q15 write a program to check the number if its prime

user_input = int(input("Enter number to check:  "))
if user_input%2==0:
    print("number is not prime")
else:
    print("number is prime")

## Q16 count the number of unique words
user_input = input("Enter your desire words to count: ")
user=user_input.replace(" ","")
# unique=user_input.split(" ")
# words=set(unique)
# u=len(words)
# print(f"Unique Words are",u)
lst=[]
for char in user:
    if char not in lst and char!='':
        lst.append(char)
print(len(lst))   


# user_input = input("Enter your desire words to count:")
# user=user_input.replace(" ","")
# words=set(user)
# print(len(words))

## Q17 #create a program that generate a fibnocci sequence upto given number of terms

def fibnocci(x):
    if x==0 :
        return 0
    elif x==1:
        return 1
    else:
        return fibnocci(x-1)+fibnocci(x-2)
        
print(fibnocci(2))

# Q18 given a number print its table
def table(num):
    for x in range(0,11):
        print(f"{num} * {x} = {num*x}")
        
print(table(5))    
    
# Q19 write a program that calculate factorial of given number

def factorial(num):
    if num ==0:
        return 1
    else:
        return num* factorial(num-1)
            
print(factorial(5))

# Q20 #create a loop that prints all prime number between 1 to 50
def Prime():
    for x in range(1, 51):
        if x%2==0:
            continue
        else:
            print(f"i am a prime {x}")
Prime()

## Q21 given  a list of words count the words with len greater then 5

def  count():
    count = 0
    lst =['hello','sharry','yasiras','khanbro','okay','haha']
    for x in lst:
        if len(x) >=5:
            count+=1
        else:
            continue
    print(count)
count()


#given a list of alph
# sort a string
# find all list items
# play the waiting game
# save the dictionary into a file --> use pickle library
# schedule a function
# send an email
# determine different probability when rolling a dice
# count the number of unique words
# write a program to generate passphrases u can use diceware(password generator)
# mmerge csv files
# solve sudoku
# build a zip archive
# download sequential files


