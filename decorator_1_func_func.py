"""
this script shows how a function decorates another function.
"""

# This function is decorator. it takes a function as input parameter.
def deco(my_function):

  # this function is executed when decorated function is called
  # so parameters here must be same as parameters in the decorated function.
  def my_function_wrapper(*args, **kwargs):
    print('from function wrapper')
    return my_function(*args, **kwargs)

  return my_function_wrapper

@deco # decorator
def multiply(a,b): # decorated function
  print(" %d x %d = %d " % ( a, b, a*b))
  return a * b

if __name__ == '__main__':
  multiply(2,5) # decorated function is called
