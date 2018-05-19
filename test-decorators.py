def our_decorator(func):
    def function_wrapper(*args):
        print("Before calling " + func.__name__)
        func(*args)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def foo(x, y, z):
    print("#:" + str(x) + " " + str(y) + " " + str(z))


@our_decorator
def bar():
    print('#dasdas')


foo("Hi", "ho", "al campo a trabajar")
bar()
