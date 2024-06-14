#sets in python --> collection of well defined objects , it is not changeable and donot allow repeated values 
#it is unordered collection of items
#sets can have multiple data types
#there is no guarantee that order will be maintained
S= {1,2,3,2,3}
print(S)
S1 ={1,2,3,True,'hello',False}
#if you want to create empty set use this
# S = set()
# print(type(S))

#accessing values of set
 
for value in S1:
    print(value)

#methods of sets
#union() and update()
S1 = {1,2,3,6}
S2 = {4,5,6}
S1.union(S2) #it performs union operation
print(S1,S2)
#now in order to update the S1
S1.update(S2)
print(S1)

#intersection of sets
C1 = {'peshawar','islamabad','lahore','karachi'}
C2 = {'multan','peshawar','murree','abottabaad'}
C1.intersection(C2)
#now if you want to update 
C1.intersection_update(C2)
print(C1)

#symmetric difference prints those items that are not similar in both the sets
C1 = {'peshawar','islamabad','lahore','karachi'}
C2 = {'multan','peshawar','murree','abottabaad'}
C1.symmetric_difference(C2)
# Note order does not matter
#if you want to update
C1.symmetric_difference_update(C2)
print(C1)

#difference and difference_update   (A-B)
C1 = {'peshawar','islamabad','lahore','karachi'}
C2 = {'multan','peshawar','murree','abottabaad'}
C1.difference(C2)
#if u want to update 
C1.difference_update(C2)
print(C1)

#isdisjoint() -->returns true and false 
C1 = {'peshawar','islamabad','lahore','karachi'}
C2 = {'multan','peshawar','murree','abottabaad'}
C1.isdisjoint(C2) #it will give false because peshawar is common in both


#issuperset() gives true and false for superset
C1 = {'peshawar','islamabad','lahore','karachi'}
C2 = {'multan','peshawar','murree','abottabaad'}
C1.issuperset(C2)

#issubset() --> give true and false if it is subset
C1 = {'peshawar','islamabad','lahore','karachi'}
C2 = {'peshawar','islamabad'}
C2.issubset(C1)

 #if you want to add item to the set use add()
C1.add('india')
print(C1)

#if you want to add more than one item use update()
C3 = {'attock','Nowshera','mardan'}

C1.update(C3)
print(C1)

#remove()/discard()
#the difference between remove and discard is that the remove raises error if element not present while discard doesnot
C1.remove('peshawar')
print(C1)

#u can pop() an element it will be removed from end but we donot which element will be present in last as sets are random
#but can check that element by storing in variable
item = C1.pop()
print(item)

#del is a keyword that delete entire dataset
del C1
print(C1) # it will raise error as C1 is deleted 

# clear() is method that clear entire items in dataset and give empty set
C2.clear()
print(C2)

#check if item exist in set
info = {'yasirx',23,'BSSE'}
if 'yasir' in info:
    print(True)
else:
    print(False)
    
    
#dictionary are ordered collection of item and these items are key value pairs
studata = {'name': 'yasir', 'age':23, 'department':"BSSE","batch":"2024"}

#accessing the items in the dictionary
print(studata['name'])#it throws error if key is not present
print(studata.get('name'))#it prints none if key is not present
# both are used to access the data
#if you want to access all the keys or values

print(studata.keys())
print(studata.values())

#you can iterate each value aswell

for key in studata.keys():
     print(f"the value corresponding to {key} is {studata[key]}")

#accessing keyvalue pairs
print(studata.items())
for key,value in studata.items():
      print(f"the value corresponding to {key} is {value}")

#dictionary methods
#u can use update() to update your dictionary
detail1 = {133:'Ammad',139:'yasir',121:"hamza"}
details2= {110:'ahmed',138:'suffian',136:"farzam"}
detail1.update(details2)
print(detail1)
#clear() it clears all items and gives empty dictionary
details2.clear()
print(details2)

#use of pop() it takes key as parameter and removes key value pair
detail1.pop(133)
print(detail1)

#popitem() it removes last keyvalue pair
detail1.popitem()
print(detail1)

#use of del keyword which will delete entire dictionary or if you give parameter key than desired key value pair will be deleted
del detail1[139]
detail1
# or u can delete entire dictionary
del detail1

print(detail1) # not defined error because it got deleted

#using for loop with else --> else can be used with loop

for i in range(2,10,2):
    print(i)
else:
    print('sorry i is finished ')
    
#note it only executes if loop iteration is completed and if u put break statement it wonot executes
