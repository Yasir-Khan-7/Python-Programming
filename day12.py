#File IO in python
 #now the file takes first argument as filename and second argument as mode it can read write or append as 'a'
f = open("testfile.txt", 'r')
print(f.read())
f.close()

#now i want to write something into the file
#note that if you are writting then this will overwrite everything older wriiten in file so use append instead
f = open("testfile.txt", 'w')
f.write("This is not good guys")
f.close()

#now i want to append some content into the file

f = open('testfile.txt','a')
f.write("hello updating the data")
f.close()

#now there is alternative of opening and closing the file using 'with' keyword

with open("testfile.txt",'a') as f:
    f.write("hello i am going again")