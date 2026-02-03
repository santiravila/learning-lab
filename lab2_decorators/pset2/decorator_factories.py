"""
Implementing a decorator factory for calling a function N times
Benefits: less rewriting, greater decorator customization

- repeat decorator factory
- print Starting set... once at the beginning
- execute function times amount of times
- print Circuit complete at the end
"""


import functools

def repeat(times: int):
    if times <= 0:
        raise ValueError("times argument has to be greater than zero")
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Starting set...")
            for _ in range(times):
                result = func(*args, **kwargs)
            print("Circuit complete")
            return result
        return wrapper
    return decorator


@repeat(times=3)
def burpees():
    print("Down, up, jump!")


burpees()