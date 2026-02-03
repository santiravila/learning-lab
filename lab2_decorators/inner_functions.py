"""
Functions can be defined and called inside other functions
"""

def parent():
    print("Parent")

    def first_child():
        print("First Child")

    def second_child():
        print("Second Child")

    second_child()
    first_child()


# second_child() NOT DEFINED OUTSIDE PARENT SCOPE
# first_child() NOT DEFINED OUTSIDE PARENT SCOPE

"""

>>> parent()
Parent
Second Child
First Child

"""
