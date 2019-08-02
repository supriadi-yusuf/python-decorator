def greeting(self, nama): # since this is a method so it takes self as argument
    print(self)
    print("Hello " + nama + ", selamat pagi.")

class Augment:
  def __init__(self, greeting_required):
    self.__greeting_required = greeting_required

  def __class_wrapper(self, *args, **kwargs):
    if self.__greeting_required:
      self.__cls.greeting = greeting

    return self.__cls( *args, **kwargs)

  def __call__(self, cls):
    self.__cls = cls
    return self.__class_wrapper

@Augment(True)
class Philo:
  pass

@Augment(False)
class Talo:
  pass

p = Philo()
t = Talo()

p.greeting("supriadi")
t.greeting("juju")
