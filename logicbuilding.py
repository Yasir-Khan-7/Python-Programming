#Note: & in Python
# The ‘&‘ symbol is a bitwise AND operator in Python, it is also known as a bitwise AND operator.
# It operates on the bitwise representation of integers.

# Note: The ‘and‘ keyword in Python is used in the logical operations. It is used to combine two logical statements, 
# it returns TRUE if both are correct and FALSE if any of the statements is wrong.

# write a program diivsible by 7 not multple of 5 from 2000 to 3200
lst =[]
for number in range(2000,3200):

    if number%7==0 and number%5!=1:
        lst.append(number)

print(lst)

# write a program to calculate its factorial
# fact of 0 and 1 is always 1
def factorial(num):
    if num ==0 and 1:
        return 1
    else:
       return num*factorial(num-1)
res = factorial(5)
print(f"The factorial of {5} is: {res}")


# program 3 write a program that takes a number 
# and creates dictionary of all previous numbers key is its index and square is its  value

Dictionary={}
def dict_number(num):
    
    for  x in range(1,num):
     
        Dictionary[x] = x*x
        
dict_number(5)    
print(Dictionary)

# check for prime factors
lst2 = []
def Prime(num):
    
        if num%num==0 and num%1==0:
            lst2.append(num)
       
Prime()
print(lst2)       
# check for palindrome
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


