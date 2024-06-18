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
# then python interpretor will change its so that other class cannot acces it


class Book:
    def __init__(self, BookTitle, author, pages, price):
        self.BookTitle = BookTitle
        self.author = author
        self.pages = pages
        self.price = price

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
