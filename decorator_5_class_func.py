class Deco: # class as decorator
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        #print(self)
        print("from class Deco")
        self.__func( *args, **kwargs)

@Deco
def hello():
    print("hello, selamat pagi semua.")

hello()
