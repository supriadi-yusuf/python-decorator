"""
function can also decorate a class.
this script shows how the function looks like.
"""

# we make this function to act like a method so it takes self as argument.
def greeting(self, name):
    print(self)
    print("Hello " + name + ", selamat pagi.")

# this function is decorator. it takes a class as input parameter.
# the class is decorated class.
def augmentclass(my_class):
  my_class.greeting = greeting # assign new attribute to the decorated class.
  return my_class

@augmentclass # decorator
class Philo: # decorated class
    pass

class Talo:
    pass

if __name__ == '__main__':
   p = Philo()
   t = Talo()

   p.greeting("supriadi")
   t.greeting("juju") # this should be error ( exception is raised )
