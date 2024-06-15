#Exceptional handling when some unexpected events occur 
#so exceptional handling deals with such events and avoid  program or system crashing
# without this the system might crash or program haults
#lets see example
a = input("Enter a number to print its table:")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e: 
       print("some Error occurs:",e)


print('some important line of code')
print("end of program")

# u can handle multiple errors aswell 

try:
    x  = int(input("Enter a integer value:"))
    a= [4,5,6]
    print(a[x])
except ValueError:
    print("the number is not integer:")
except IndexError:
    print("there is an index error")
    

#finally keyword --> it is always executed no matter what happens 
# something is wrapped in a function and value is returned  but finally will always execute if error occurs or not
def fun1():
    try:
        l =[1,2,3,4]
        x = int(input("enter the index number"))
        print(l[x])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i will always execute")
        
result = fun1()
print(result)

#raising custom errors
#in python we can raise custom errors using 'raise' keyword 
# when you want to stop the program at some point due to error

value = int(input("Enter value between 4 and 10"))
if(value<4 or value>10):
    raise ValueError("please enter between 4 and 10")
#quiz 

str  = input("Enter quit in small letter:")

if(str!='quit'):
    raise SyntaxError("please write quit in small letter")


#defining Custom Exception --> when at some point you want to write raise custom exceptions
#learn more about it 