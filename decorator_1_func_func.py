"""
this script shows how a function decorates another function.
"""

def deco(func):
  """
  This function is decorator
  """

  def func_wrapper(*args, **kwargs):
    print('from func wrapper')
    return func(*args, **kwargs)

  return func_wrapper

@deco
def multiply(a,b):
  print(" %d x %d = %d " % ( a, b, a*b))
  return a * b

if __name__ == '__main__':
  multiply(2,5)
