# create a basic class
class Book:
    def __init__(self, BookTitle):
        self.BookTitle = BookTitle


# create instance of the class
book1 = Book("The journey ")
book2 = Book("The End of Game")

# print the class and property
print(book1)
print(book1.BookTitle)

# updating more properties and adding methods to the class

# Note: using _nameofattribute (single underscore) it means that the attribute is for internal use of class
# Note: hasattr() is used to check if the attribute exists or not
# Note: if you use double underscore before start of name of attribute or method
# then python interpretor will change its so that other class cannot access it


class Book:
    def __init__(self, BookTitle, author, pages, price):
        self.BookTitle = BookTitle
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "this is secret attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


book3 = Book('high on', "james", 1239, 29.9)
print(book3.getprice())
book3.setdiscount(0.25)

print(book3.getprice())

# print(book3.__secret) # it will give error because python hides it
# to check it use class name before u can then access itt
print(book3._Book__secret)  # u will get the access check it



#now using the type() function and isinstance() to check the type of instance

class book:
    def __init__(self,title):
            self.title = title
class newspaper:
    def __init__(self,name):
        self.name = name
b1 = book("the Red line")
b2 = book("cross over")
n1 = newspaper("the dawn")

n2 = newspaper("one news")

#checking type
print(type(b1))        
print(type(n1))
#comapring both types to check if they are same or not
