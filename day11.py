#local vs Global variable 
# it is variable that is defined within the function and is accessable within function scope
# plus is destroyed when function return

x = 5 #global variable

def my_fun():
    y=3 
    print("this is local variable: ", y)
    
my_fun()
print(x)# it is global website and can be accessed
# print(y)#it cannot be printed as it is local variable and gives error

#now in order to convert the local into global use Global keyword

x = 5 #global variable

def my_fun():
    global x
    x =6
    
my_fun()
print(f"Now i am changed to {x}")#now the x value changes due to use of gobal keyword