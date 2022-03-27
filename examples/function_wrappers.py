def function_decorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")
    return inner1

def func_to_be_used():
    print("Inside the functino")

our_function = function_decorator(func_to_be_used)

our_function()

@function_decorator
def our_function2():
    print("Bruh emoji")

our_function2()