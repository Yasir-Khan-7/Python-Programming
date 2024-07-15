import math


#Note: & in Python

# The ‘&‘ symbol is a bitwise AND operator in Python, it is also known as a bitwise AND operator.
# It operates on the bitwise representation of integers.

# Note: The ‘and‘ keyword in Python is used in the logical operations. It is used to combine two logical statements, 
# it returns TRUE if both are correct and FALSE if any of the statements is wrong.

# write a program diivsible by 7 not multple of 5 from 2000 to 3200
# lst =[]
# for number in range(2000,3200):

#     if number%7==0 and number%5!=1:
#         lst.append(number)

# print(lst)

# # write a program to calculate its factorial
# # fact of 0 and 1 is always 1
# def factorial(num):
#     if num ==0 and 1:
#         return 1
#     else:
#        return num*factorial(num-1)
# res = factorial(5)
# print(f"The factorial of {5} is: {res}")


# program 3 write a program that takes a number 
# and creates dictionary of all previous numbers key is its index and square is its  value

# Dictionary={}
# def dict_number(num):
    
#     for  x in range(1,num):
     
#         Dictionary[x] = x*x
        
# dict_number(5)    
# print(Dictionary)

# check for prime factors
# lst2 = []
# def Prime(num):
#     for x in range(2,num):
        
#         if  num%x==0:
#             return False
#         else:
#             return True
       
# res =Prime(13)
# print(res)    
# check for palindrome

# def palindrome(str):
#         if str  == str[::-1]:

#             print("String is palindrome")
         
#         else:
#             print("is not palindrome")
        
# palindrome("yasir")

# Question
# Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:


# lst1 =[]
# lst2 = []

# for x in range(0,5):
#     number = input(f"Enter  number:{x+1} ")
#     lst1.append(number)
#     lst2.append(number)
#     tup = tuple(lst2)
    
# print(lst1)
# print(tup)

# #Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# class Stringbox:
#     def __init__(self):
#         self.str = " "

#     def getString(self):
#         self.str = input("Enter the String: ")
#     def printString(self):
#         print(self.str)
    
# obj = Stringbox()
# obj.getString()
# obj.printString()



# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

# def calculateQ(*args):
#     print(args)
#     new_lst = []
#     C = 50
#     H = 30 
#     for x in args:
#         print(x)
#         Q = math.sqrt((2*C*x)/H)
#         new_lst.append(str(int(round(Q))))
#     return new_lst

# res =calculateQ(23,24,33)
# print(res)


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.


# def two_dimensional(num1,num2):
#     twoD = [[0,0,0],[0,0,0],[0,0,0]]
#     for x in range(num1):
#         for y in range(num2):
         
#             twoD[x][y] = x*y     
          
#     print(twoD)
# two_dimensional(3,3)  
    
# Write a program that accepts a comma separated sequence of words 
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


