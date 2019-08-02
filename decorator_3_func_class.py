
"""
function can also decorate a class.
this script shows how function decorates a class.
"""

def greeting(self, nama): # since this is a method so it takes self as argument
    print(self)
    print("Hello " + nama + ", selamat pagi.")

def augmentclass(cls):
  """
  this function is decorator.
  """

  cls.greeting = greeting
  return cls

@augmentclass
class Philo:
    """
    this class is decorated by function.
    """
    pass

class Talo:
    pass

if __name__ == '__main__':
   p = Philo()
   t = Talo()

   p.greeting("supriadi")
   t.greeting("juju") # this should be error ( exception is raised )
