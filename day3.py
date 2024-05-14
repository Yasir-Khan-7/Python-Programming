#string method - continue 
# replace() method -> IT replaces all occurance of a string with another string
a ='yasir, khan'
print(a.replace("yasir",'ahmed'))
 #all occurance changes
 
 # split() it splits the string at specific instance and return the seperated string as list
print(a.split(","))

#capitalize() -->capitalizes first letter of string
heading =  "hello how are you hello"
print(heading.capitalize())

#center() it centers the text 
print(heading.center(50))

# count()-->it counts the characters of string how many times it occurs
print(heading.count('h'))

#endswith()---> it gives whether the desired string ends with the string given or not give true and false
#startswith()-->it gives whether the desired string ends with the string given or not give true and false

text2 = "Welcome to the console ***"
text3 = "Hello how are you"
print(text2.endswith("***"))
print(text3.startswith("Hello"))
text2 = "Welcome to the console ***"
print(text2.endswith('to',4,10))# check in between aswell

#find() --> it finds the first occurance of the desired string and return its index if not present then returns -1
heading = "Hello yasir is this and is that "
print(heading.find('is'))

#index()-->same as find() but if string is absent then raise an exception in output
# print(heading.index("xyz"))

#isalnum()-->this check if string is made up of alpha-numeric(A-Z,a-z,0-9) then retuns true otherwise false

print(heading.isalnum())#--> gives false because of spacing

#isalpha()-->checks if A-Z, a-z  is present then return true otherwise returns false

text = 'yasir0'
print(text.isalpha())#--> gives false because of  0 present

#islower()--> returns true if all the characters are in lower case otherwise false
#isupper()-->  returns true if all the characters are in upper case otherwise false
a = 'sharjeel khan'
b ="SHAR"
print(a.islower()) 
print(b.isupper())
#isprintable()--> checks if all the characters in string is printable or not return true otherwise false
b =" hello how are you"
c=" hello how are yo \n iam good"
print(b.isprintable())
print(c.isprintable())

#isspace()-->it checks whether you enter whitespaces(note: complete whitespaces no character in it) or not so return true otherwise false
txt = "    "
print(txt.isspace())

#istitle()-->it returns true if the first letter of each word is capitalized
who = "World Health Organization"
print(who.istitle())

#swapcase()-->converts the upper into lower and lower into upper
f = "yasir khan"
print(f.swapcase())

#title()-->it capitalize first letter of each word in string
v = "today is tuesday"
print(v.title())

#if and else statements
#condtional operators >,<,<=,>+,!=
bananaprice = 120
budget = 110 
if(budget>=bananaprice):
    print("you can buy bananas")
else:
    print("sorry you are out of budget") 

#elif  statements
appleprice = 50
budget = 140

if(budget-appleprice==150):
    print("you can definately buy apple")
    
elif(budget-appleprice>80):
    print(" you can buy apple")
    
else:
    print("sorry you are out of budget")
    
    
#nested if else statement 
if(budget-appleprice==150):
    print("you can definately buy apple")
    
elif(budget-appleprice>90):
    if(budget-appleprice<=100):
        print(" you can buy apple")
    
else:
    print("sorry you are out of budget")
    
#Exercise Goodmorning Sir using if else
import time #built in module for time checking
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

#match case statement--> just like switch cases but there is no break in it only matches case will execute
x = 5
match x:
    case 0:
        print('x is xero')
    case 4:
        print("value is 4")
    case _:
        print(x)
        
# u can use if in match case statement

x = 80
match x:
    case 0:
        print('x is xero')
    case 4:
        print("value is 4")
    case _ if(x!=90):
        print(x,"x not equal to 90")
    case _ if(x!=80):
        print(x)
    case _:
        print(x)