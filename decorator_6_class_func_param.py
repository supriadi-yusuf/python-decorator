class Deco: 

   def __init__(self, p1, p2):
     self.__p1 = p1
     self.__p2 = p2 
 
   def __func_wrapper(self, *args, **kwargs):
     print((self.__p1, self.__p2))
     return self.__func( *args, **kwargs)

   def __call__(self, func): 
     self.__func = func
     return self.__func_wrapper

 
@Deco(1,10)
def f1(a,b):
   print(a)
   print(b)
   return a * b

f1(100,1000)

