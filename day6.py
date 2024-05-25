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

