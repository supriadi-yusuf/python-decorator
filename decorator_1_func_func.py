def deco(func):

  def func_wrapper(*args, **kwargs):
    print('from func wrapper')
    return func(*args, **kwargs)

  return func_wrapper

@deco
def multiply(a,b):
  print(" %d x %d = %d " % ( a, b, a*b))
  return a * b

multiply(2,5)
