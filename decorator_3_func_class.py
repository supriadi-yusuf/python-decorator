def greeting(self, nama): # since this is a method so it takes self as argument
    print(self)
    print("Hello " + nama + ", selamat pagi.")

def augmentclass(cls): 
  cls.greeting = greeting
  return cls

@augmentclass
class Philo:
    pass

class Talo:
    pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")
