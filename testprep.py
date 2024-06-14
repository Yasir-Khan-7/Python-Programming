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
#split method
name = 'yasir sharjeel'
print(name.split(" "))

#capitalize method

print(name.capitalize())

print(" banda kla putr bn jao")


print('hello jani')

print(name.center(100))

