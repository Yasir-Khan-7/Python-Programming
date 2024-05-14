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


text2 = "Welcome to the console ***"
print(text2.endswith("***"))

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

a = 'sharjeel khan'
print(a.islower())

#isprintable()--> checks if all the characters in string is printable or not return true otherwise false
b =" hello how are you"
c=" hello how are yo \n iam good"
print(b.isprintable())
print(c.isprintable())
