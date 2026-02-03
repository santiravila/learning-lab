"""
Intro to Decorators
"""

def decorator1(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    
    return wrapper


def hello():
    print("Hi")


hello = decorator1(hello)  # hello points to wrapper
# calling hello() is like calling wrapper() with func = hello() 

# =====================================================================
# Syntactic sugar, (@decorator2) == (bye = decorator2(bye))

def decorator2(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    
    return wrapper

@decorator2
def bye():
    print("Bye")


# =====================================================================

from decorators import do_twice

# No arguments and side effect
@do_twice
def cheers():
    print("Cheers!")

# With arguments and side effect
@do_twice
def add(a: int, b: int):
    """
    Add two values
    """
    print(a + b)

# With arguments and return value
@do_twice
def multiply(a: int, b: int) -> int:
    """
    Multiply two values
    """
    print("Multiplying...")
    return a * b

# Learned: docstrings inside functions are displayed with the __doc__ special method
# print(add.__doc__)
# print(multiply.__doc__)