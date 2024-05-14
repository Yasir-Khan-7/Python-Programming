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

#find() --> it finds the first occurance of the desired s tring