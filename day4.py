#while loops
i=1
while(i<5):
    print(i)
    i=i+1
 #now create a count variable
count = 10 
while(count>0):
     print(count)
     count = count-1
#use of else statement with the while loop
# if while loop becomes false then the else statement will execute

count = 0 
while(count<5):
     print(count)
     count = count+1
else:
    print("you are out ")
    
#do while loop in python
# do while concept is that it excute block of statement at least once

#break and continue
#break is to exit the loop and continue is to exit the iteration

#break
for j in range(12):
    if(j==10):
        print('loop ko chor ky nikal jao')
        break
    print("5 X", j, "=", 5*j)
    
#continue
for m in range(12):
    if(m==10):
        print('skip kro iteration ko ')
        continue
    print("3 X", m, "=", 3*m)

#emulating do while loop
#it will execute the print once always then check condition
i=0
while True:
    print(i)
    i=i+1
    if(i%10==0):
        break

#functions --->when u want to run block of code too many times in your code so better to wrap in a function
def calgmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


def isgreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater")
isgreater(5,7)
calgmean(5,7)
isgreater(3,8)
calgmean(3,8)

#if you want to write a function later in a code then use 'pass keyword'
def fun1():
    pass
#it will not give error rather it will pass to next statement
#arguments in the functions

# 1: default argument 
def sum(a=4,b=6):
    print(a+b)
sum()
#now if you give in values in function and send as parameter aswell so sended will overide the value u assigned   
def sum(a=4,b=6):
    print(a+b)
sum(6,7)
#now if you give one value in function  the other will be considered the value assigned in the parameter
def sum(a=4,b=6):
    print(a+b)
sum(7) # value a will be changed
sum(b=8)# value b will be changed 

#2 : keyword argument in which order doesnot matter

def sub(a,b):
    print(a-b)

sub(b=4,a=10)

#3 required arguments which is must to be passed otherwise error will generate correct order plus
def sub(a,b):
    print(a-b)

sub(4)# error will generate

#4 variable- length argument it check numbers length
def average(*numbers):# the type of number is tuple
    sum = 0
    for i in numbers:
        sum = sum+i
    print('average is',sum/len(numbers))

average(4,5,6,10)
#using dictionary 
def details(**detail):# the type of number is dictionary
    print(" hello your fname is",detail['fname'],"and lastname is",detail['lname'])

details(fname='yasir',lname='khan')
#now return statement
sum =0
def fun1(x):
    global sum
    sum = sum+x
    return sum
z =fun1(4)
print(z)

#list --> u want to store multiple data in a single item
#order collection of data index by index
#list are created by [value1,value2,value3]
#list are changeable it means it can be altered after creation

list1  = [4,5,6,7]
print(list1)
print(list1[:])
print(list1[0])
print(list1[2])
print(list1[3])
print(list1[-3])# tip use len to calculate negative indexes
print(list1[len(list1)-3])
print(list1[1:5:2])#jumping indexes

list1.append(9)# it adds new member so it can be changed altered
print(list1)

#checking in the list 
if 8 in list1:
    print('hellow')
else:
    print('bye')
    
#list comprehension --> you create new list on the fly from iterable list
lst =[i for i in range(10)]
print(lst)
    
#now you will understand
list3 = ['hello','bye','ok','no','takecare']
print(list3)
newlistwith_o =[newitem for newitem in list3 if 'o' in newitem]
print(newlistwith_o)

#list methods
#append method it add new item to list
l = [1,2,3,4,5,7,6]
l.append(9)
print(l)
#sort method
l.sort()
print(l)
#now reverse method
l.reverse()
print(l)
#index method this gives the first occurance of the list item
print(l.index(3))

# count the number of items in the list 
print(l.count(1))

#copy method
m = l.copy()
m[0] =20
print(m)

#insert() you want to insert a value in any index
l.insert(2,677)
print(l)

#extend method u want to extend a list 
m = [199,188,177]
l.extend(m)
print(l)

# concatenating two list 
h =[1,2,3]
j =[4,5,6]

i = j+h
print(i)