#our first python code 
print('hello world!')# it is function that print display output
#comment for single line comment use ""

#comment for single line comment use "#" and for multiple line comment use triple single quote ''' '''
'''hello how r you 
this is actually 
multiline comment
'''

#Escape Sequence use of \n
print('hello yasir \nwhat are you doing')
#now more about print statement
print('hello world!',5,7, sep='&', end="000")# seperator is used how multiple value is seperated 
# and end is used  how the string should end 

#Variables and Data types
# variable are just like a container that allows you to store data
#data type is the type of data that variables holds

#1 numeric data
a= 5# integer
print(a)
b = 3.9# float
print(b)
c= complex(5,2)# complex number
print(c)

#2 string data 
print('hello yasir')

#3 boolean data
a =True
print(a) 

#4 Sequenced data :list and tuples
#list is ordered(index wise) collection of data that is changeable and allow multiple data types ,allow duplicates
list1 = [8,7,6,[4,5],['apple','banana']]
print(list1)
#tuples it is exactly same as the list but is unchangeable once created
tuple1 = (('apple','banana'),('orange','grape'))
print(tuple1)

#5Mapped data :dict 
#it is ordered collection of data containing key value pair
dict1 ={'name':'yasir',"age":23}
