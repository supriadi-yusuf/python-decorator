def greeting( self, nama): # since this is a method so it takes self as argument
    print(self)
    print("Hello " + nama + ", selamat pagi.")

class Augment:
  def __init__(self, cls): 
    self.__cls = cls
    self.__cls.greeting = greeting
    
  def __call__(self, *args, **kwargs):
    cls_obj = self.__cls( *args, **kwargs)
    return cls_obj

@Augment
class Philo:
    pass

class Talo:
    pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")
