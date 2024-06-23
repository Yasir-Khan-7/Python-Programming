# write a program diivsible by 7 not multple of 5 from 2000 to 3200
lst = []
for i in range(2000, 3201):
    if i % 7 == 0 & i % 5 == 0:
        lst.append(i)
print(lst)

# write a program to calculate its factorial
# fact of 0 and 1 is always 1


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)


factorial(4)

# program 3 write a program that takes a number and creates dictionary of all previous numbers key is its index and square is its  value


def dictionary(num):
    dic = {}
    for i in range(1, num+1):
        dic[i] = i*i
    return dic


print(dictionary(5))


# check for prime factors
# check for palindrome
# sort a string
# find all list items
# play the waiting game
# save the dictionary into a file --> use pickle library
# schedule a function
# send an email
# determine different probability when rolling a dice
# count the number of unique words
# write a program to generate passphrases u can use diceware(password generator)
# mmerge csv files
# solve sudoku
# build a zip archive
# download sequential files

print("hello world!")
print("temporary")
