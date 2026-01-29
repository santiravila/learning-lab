"""
measure log long each workout function takes to execute
"""


import functools
import time


# my decorator
def timer(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"{func.__name__} took {duration} seconds")
        return result
    return wrapper


@timer
def do_workout():
    time.sleep(2)
    return "Workout Complete"


@timer
def add(a: int, b: int) -> int:
    print("Loading result...")
    time.sleep(2)
    return a + b    


result = do_workout()
print(result)
result_sum = add(66, 23)
print(result_sum)
