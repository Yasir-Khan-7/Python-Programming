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