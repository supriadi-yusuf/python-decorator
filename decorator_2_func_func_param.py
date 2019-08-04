"""
decorator can take parameter.
this script shows how function decorator that takes parameter looks like.
this script also shows how to pass paramater into decorator.
"""

# this is function decorator.
# parameters we define here are parameters for decorator.
def deco( param1, param2):

  # this function takes another function as input parameter.
  # the paramater here is decorated function.
  def get_decorated_function(my_function):

    # this function is executed when decorated function is called
    # so parameters here must be same as parameters in the decorated function.
    def my_function_wrapper(*args, **kwargs):
      print('from function wrapper')
      print('param1 : %s, param2 : %s' % ( param1, param2))
      return my_function(*args, **kwargs)

    return my_function_wrapper

  return get_decorated_function

@deco(10,100) # decorator taking parameters
def multiply(a,b): # decorated function
  print(" %d x %d = %d " % ( a, b, a*b))
  return a * b

if __name__ == '__main__':
  multiply(2,5)
