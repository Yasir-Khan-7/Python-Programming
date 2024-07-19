#lambda function it is one line anonymous function 
#it is useful because it can be send as an argument 
add_1  = lambda x: x+1

print(add_1(2))

# #difference betweeen normal and lambda function 
def add_1(x):
    return x+1
# #this and above lambda are same but lambda is useful when passing function as paramenter

lst_numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda x:x**2,lst_numbers))
print(result)



#map func is iterable it takes function and iterable values 
# to read its result print in form of list or tuples etc
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))


#filter method it filter out the values based on true and false --> to check if certain value is accepted or not

def check(x):
    if x%2==0:
        return True
    else: 
        return False
    
res = filter(check,[1,2,3,4,5,6,7])
print(list(res))



#so lamba function is useful here

result = filter(lambda x: x%2==0,[4,6,8,9,2,1])
print(list(result))