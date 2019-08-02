"""
decorator can take parameter.
this script shows how function decorator that takes parameter looks like.
this script also shows how to pass paramater into decorator.
"""

def deco(prm1,prm2):
  """
  this is function decorator that takes parameter.
  """

  def func_arg(func):
    def func_wrapper(*args, **kwargs):
      print('from func wrapper')
      print('param1 : %s, param2 : %s' % (prm1,prm2))
      return func(*args, **kwargs)

    return func_wrapper

  return func_arg

@deco(10,100)
def multiply(a,b):
  print(" %d x %d = %d " % ( a, b, a*b))
  return a * b

if __name__ == '__main__':
  multiply(2,5)
