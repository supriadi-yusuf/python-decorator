"""
class also can decorate another class.
this script shows how a class decorating another class looks like.
"""

# we make this function to act like a method so it takes self as argument.
def greeting( self, nama):
    print(self)
    print("Hello " + nama + ", selamat pagi.")

# this class is decorator
class Augment:

  # this method takes a class as input parameter
  # the input parameter is decorated class
  def __init__(self, my_class):
    self.__class = my_class
    self.__class.greeting = greeting

  # this method is called when the decorated class is instantiated
  # so parameters in this method must same as parameter of __init__ method in decorated class
  def __call__(self, *args, **kwargs):
    my_obj = self.__class( *args, **kwargs)
    return my_obj

@Augment # decorator
class Philo: # decorated class
    pass

class Talo:
    pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")  # this should be error ( exception is raised )
