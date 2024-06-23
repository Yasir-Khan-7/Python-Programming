#operators 
print(5+6)# addition

print(5-6)# subtraction
print(5*6)# multiplication
print(5/6)# division
print(5//6)# floor division it remove the decimal point value
print(5**3)# exponenetial ooperator it will multiply 5x5x5 three times
print(5%3)# modulus it gives reminder

#Exercise =1  create calculator that add,subtract,multiply,divide
a = int(input("Enter first number\n "))
b= int(input("Enter  second number\n "))
print("the sum of ",a,"+",b," is ",a+b)
print("the subt of ",a,"-",b," is ",a-b)
print("the mul of ",a,"*",b," is ",a*b)
print("the divi of ",a,"/",b," is ",a/b)
# done
#type casting  to convert one data type into another data type
#Note: while conversion the data inputed should be valid

a = int("1")
print(type(a))
a = str(456)
print(type(a))
#String in python 
#anything that you enclose in a single or double quotes becomes string
a = "hello world!"
b = 'hello world!'
# multiline string --> enclose the string into triple single or double quotes
text = """hello my name is yasir
i am learning python programming
in order to achieve the journey towards data science
"""
print(text)


#accessing the characters of string
# string is like an array of characters
c = 'yasir'
print(c[0])

# looping through characters you can access each character if there is long string using loop
text = """hello my name is yasir
i am learning python programming
in order to achieve the journey towards data science
"""
for character in text:
    print(character)
    
#Slicing 
fruit = 'mango'
print(len(fruit))
print(fruit[0:2])# it includes 0 but not 2 work as 0 to n-1
print(fruit[:4])# python automatically insert 0 at start 
print(fruit[:])# it start 0 till length
print(fruit[-3:-1])#it starts from reverse negative slicing

#string methods
# Note: strings are immutable and cannot be changed in place but new string can be created using methods
z = '!!!!!yasir!!!!!!'
print(len(z))# it gives the length of the stirng
print(z.upper())#converts into uppercase
print(z.lower())#converts into lowercase

print(z.strip("!"))# it strips the leading and trailing both characters 
print(z.rstrip("!"))# it strips the trailing  characters 
