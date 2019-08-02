def greeting(self, nama): # since this is a method so it takes self as argument
    print(self)
    print("Hello " + nama + ", selamat pagi.")

def augmentclass(greeting_required):

  def class_wrapper(cls):
    if greeting_required:
      cls.greeting = greeting

    return cls

  return class_wrapper

@augmentclass(True)
class Philo:
  pass

@augmentclass(False)
class Talo:
  pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")
