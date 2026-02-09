"""
Query params are used to pass additional info to a server as part of a URL. 
Useful for filtering, sorting, pagination, etc...

query params can have defaults (unlike path params)
"""

from fastapi import FastAPI


app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]