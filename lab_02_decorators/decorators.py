import functools

# good practice to call inner function wrapper_function-name
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

# *args: accept any number of arguments and unpack them

# **kwargs: accept any number of key-value pairs as arguments and unpack them

# return func(*args, **kwargs): return the return value of the last function call

# @functools.wraps(func): Preserve function identity during introspection after decoration. REPL >>> func -> <function func at 0x00000001>