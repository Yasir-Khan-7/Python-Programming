#string are immutable
#anything u enclose in double or single quote is called string
name = 'yasir'
friend ='sharjeel'
#when u want to add double quote
print("""hello 
    jani kaisay ho
    """)
    #indexing in string
print(name[0])

#looping through string
for i in name:
    print(i)
print(len(name))

#methods in string

#len()
print(len(name))
#touppercase()
print(name.upper())#it creates a copy of it as string is immutable
#now lower method
print(name.lower())

#strip method strip from all side
d = 'hello!!!'
print(d.strip("!"))

#rstrip -->rstrip  only from end
d = "!!!!hello!!!!"
print(d.rstrip("!"))

#replace()
name = 'john'
newname ='sharjeel'
print(name.replace(name, newname))
#split method it splits the text
name = 'yasir is sharjeel'
print(name.split(" "))

#capitalize method it capatalize the first letter

print(name.capitalize())




print('hello jani')
#IT Center the text
print(name.center(100))

#endswith() returns true and false for checking
print(name.endswith("@"))
#now see this 
print(name.endswith('to',2,8))#ending index will be checked 

#find() method give index else if not found give -1

print(name.find("is")) 

#index() method is same like but gives exception on if not found
print(name.index("jjgh"))

#isalnum() give true if entire string only is Either CAPITAL A-Z or Small a-z or 0-9
str = 'HELLO'
str2 = '096'
print(str.isalnum())
print(str2.isalnum())

#isalpha give true if entire string only is Either CAPITAL A-Z or Small a-z
print(str.isalpha())
print(str2.isalpha())#false because number not in isalpha

#islower() checks whether all string are lower character and gives true if present otherwise false
print(str.islower())#false because of capital

#isupper() checks whether all string are upper character and gives true if present otherwise false
print(str.isupper())#true because of upper

#isprintable -- gives true if characters are printable means it doesnot include special characters
str3 = 'hello world brother'
str4 = "hello i am special \n ok"
print(str3.isprintable())
print(str4.isprintable())#false because of \n it is not printable character

#ispace()

