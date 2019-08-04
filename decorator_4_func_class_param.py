"""
function that decorates a class can also takes parameter.
this script shows how the function decorator looks like.
"""

# we make this function to act like a method so it takes self as argument.
def greeting(self, nama):
    print(self)
    print("Hello " + nama + ", selamat pagi.")

# this function is decorator. it takes parameter.
# the parameter here is decorator parameter.
def augmentclass(greeting_required):

  # this function takes parameter.
  # the parameter here is a class to be decorated.
  def get_decorated_class(my_class):
    if greeting_required:
      my_class.greeting = greeting

    return my_class

  return get_decorated_class

@augmentclass(True) # decorator taking parameter
class Philo: # decorated class
  pass

@augmentclass(False) # decorator taking parameter
class Talo: # decorated class
  pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")  # this should be error ( exception is raised )
