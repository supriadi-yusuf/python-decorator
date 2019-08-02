def deco(func):
    def wrapper(*args, **kwargs):
        print("wrapper is being executed")
        return func(*args, **kwargs)

    print("hello from decorator")
    return wrapper

ans = input("use deco as decorator?(y/t)")
if ans == 'y':
    @deco # this line causes string "hello from decorator" is printed
    def t1():
       pass

    ans = input("execute t1?(y/t)")
    if ans == 'y':
        t1() # this line causes string "wrapper is being executed" is printed
