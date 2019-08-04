"""
decorator class can take parameter.
this script shows how decorator class that takes parameter looks like.
in this example the class decorates a function.
"""

# this class is decorator
class Deco:

   # this method takes parameters.
   # these parameters are decorator's parameters
   def __init__(self, p1, p2):
     """ this method takes parameters. these parameters are decorator's parameters. """
     self.__p1 = p1
     self.__p2 = p2

   # this method is called / executed when decorated function is called.
   # so paramters in this method must be same as parameters in the decorated function.
   def __function_wrapper(self, *args, **kwargs):
     print((self.__p1, self.__p2))
     return self.__func( *args, **kwargs)

   # this method takes function as parameter
   # the function is decorated function
   def __call__(self, my_function):
     self.__func = my_function
     return self.__function_wrapper


@Deco(1,10) # decorator
def f1(a,b): # decorated function
   print(a)
   print(b)
   return a * b

f1(100,1000)
