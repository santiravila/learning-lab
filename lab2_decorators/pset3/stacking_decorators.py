"""
# pset: the HTML formatter
# Implementing stacked decorators
## Benefits: separating behavior, splitting a giant decorator into several

- decorators are applied from the bottom up
- implement decorators @bold and @italic that wrap the return string
- @bold wraps in <b>...</b>
- @italic wraps in <i>...</i>
- Define function get_text() that retuns "Hello"
- stack the decorators in different order
"""


import functools # I KEEP FORGETTING ADDING THIS ONE FOR PRESERVING IDENTITY AND DOCS


def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper


@bold
@italic
def say_hello():
    return "Hello"

@italic
@bold
def say_bye():
    return "Bye"


print(say_hello())
print(say_bye())