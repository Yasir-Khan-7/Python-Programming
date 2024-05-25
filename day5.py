#tuples in python  are ordered collection of items that are made with() and seperated by commas and is not changeable
tup =(1,)

print(type(tup))
#as it is unchangeable once created so
tup[0] = 6 #this will give error
 # u can have multiple item in tupple 
tup1 =(2,4,5,'hello',True)
#indexing is same in tuples as in list
print(tup1[0],tup1[1])
#check in tupple 
if 'hello' in tup1:
    print('yes bro i am in')
else:
    print('sorry bro i am out')

#methods of tuples (manipulating tuples)
#if you want change tuples first you have to convert it into lists then to tuples
countries = ('spain','italy','france','Pakistan','England','germany')
temp = list(countries)
temp.append('America')
temp.pop(2)
temp[1]= 'india'
countries = tuple(temp)
print(countries)
#instead of this u can create concatenate two tuples which will make new tuple
num1 = (1,2,3)
num2 = (3,4,5)
numbers = num1 +num2
print(numbers)
#count() it give count of any number
print(numbers.count(3))
#index() it give the first occurance of any number (its index) and raises error if element is not in tuple
print(numbers.index(3))
#u can give starting and ending in indexing
print(numbers.index(3,1,4))
#len() u can use it to check the length of the tuple
print(len(numbers))

# python developer faces a problem in encountering the formating of strings
letter = 'hello my name is {} and i am from {}'
country = 'Pakistan'
name ='Yasir'
letter.format(name,country)
#along with that u can assign numbers aswell
letter = 'hello my name is {1} and i am from {0}'
letter.format(country,name)
# but this makes problem remember when u have very long chunk of code 
# so python f-string was introduced to resolve this problem
# which allows you to insert variable into string write f"string"
txt = f"hello my name is {name} and i am from {country}"
print(txt)
#f-string was introduced in python 3.6 
price =49.09999
print(f"value is {price:.2f} ")#it will give answer in upto two decimal floating point
# when you want to show curly brackets in your string use double curly brackets

print(f"hello my name is {{name}} and i am from {{country}}")

#docstring are string literals that are written just after definition of function, class, module or method
def fun2():
    '''it is simple function that prints hello world'''
    print('hello world!')

print(fun2.__doc__)

# what is PEP 8 it is document that provides best practice on how to write python code
import this  #it is called ZEN of python which is poem about 

#Recursion --> a function that calls itself or other function recursively
def fibnocci(num):
    if(num==1):
        return 1
    elif(num==0):
        return 0
    else:
        return (fibnocci(num-1)+fibnocci(num-2))
res = fibnocci(6)
print(res)

