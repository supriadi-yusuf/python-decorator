"""
class can also become a decorator.
in order to do that, instance of the class must be callable.
the class must implement __call__ method in order to make it's instance callable.
In this script we see how a class decorates a function.
we can see how the class looks like.
"""

# this class is decorator
class Deco:

    # this method takes a function as input parameter
    # the function is decorated function
    def __init__(self, my_function):
        self.__func = my_function

    # this method makes instance of class become callable.
    # this method will be called when the instance is called.
    # the instance is called when the decorated function is called.
    # so parameters of the function must be same as parameter of this method.
    def __call__(self, *args, **kwargs):
        print("from class Deco")
        return self.__func( *args, **kwargs)

@Deco # decorator
def hello(): # decorated function
    print("hello, selamat pagi semua.")

hello()
