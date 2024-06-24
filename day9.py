# In Python, the construct if __name__ == "__main__":
# is used to check if a script is being run directly (not imported as a module).
# If it is run directly, the code inside this block will execute. This is useful for running tests or main functions.
# what does it do if you import this at some other place so wonot execute full script until it is directly runed from the main script
def fun1():
    print("hello this is simple function")


print(__name__)
if __name__ == "__main__":
    fun1()
