"""
- Python functions as First-Order objects (or first-class citizens)
- they can be passed as arguments, returned from functions, stored in data structures, be defined inside other functions...
"""
def test():
    def data():
        print("Returning 1...")
        return 1
    
    return data

collection = []
data = test()
collection.append(data())

print(collection[0])

def hello(name):
    print(f"Hello {name}")


def bye(name):
    print(f"Bye {name}")


def greet_me(some_func):
    return some_func("Me")


"""
Functions passed as arguments are not CALLED, they are REFERENCED (without parentheses)

python3 -i greeters.py
>>> greet_me(hello)
Hello Me
>>> greet_me(bye)
Bye Me

"""