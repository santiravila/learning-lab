""" 
- Functions can return inner functions
"""

def parent(num):
    def first_child():
        print("Hello")

    def second_child():
        print("Bye")

    if num == 1:
        return first_child
    else:
        return second_child


"""
the return value is a reference to the inner functions inside parent

>>> first = parent(1)
>>> second = parent(2)
>>> first
<function parent.<locals>.first_child at 0x74489143b420> REFERENCE
>>> second
<function parent.<locals>.second_child at 0x74489143b380> REFERENCE
>>> first() REFERENCE CALL
Hello
>>> second() REFERENCE CALL
Bye

"""