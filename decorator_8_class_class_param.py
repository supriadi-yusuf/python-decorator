"""
decorator class can also take parameters.
this script shows how the decorator class looks like.
"""

# we make this function to act like a method so it takes self as argument.
def greeting(self, nama):
    print(self)
    print("Hello " + nama + ", selamat pagi.")

# this class is decorator
class Augment:

  # this method takes parameter
  # the parameter is decorator's parameter
  def __init__(self, greeting_required):
    self.__greeting_required = greeting_required

  # this method is called when decorated class is instantiated.
  # so parameters of this method must be same as parameters of __init__()
  # method of decorated class
  def __class_wrapper(self, *args, **kwargs):
    if self.__greeting_required:
      self.__class.greeting = greeting

    return self.__class( *args, **kwargs)

  # this method takes class as input parameter.
  # the input parameter is decorated class
  def __call__(self, my_class):
    self.__class = my_class
    return self.__class_wrapper

@Augment(True) # decorator
class Philo: # decorated class
  pass

@Augment(False) # decorator
class Talo: # decorated class
  pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")  # this should be error ( exception is raised )
