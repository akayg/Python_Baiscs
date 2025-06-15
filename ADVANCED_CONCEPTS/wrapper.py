def mainlog(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return wrapper

@mainlog
def say_hello():
    print("Hello!Commander")

say_hello()
