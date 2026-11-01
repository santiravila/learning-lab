from fastapi import FastAPI
from infrastructure.database import Base, engine
from customers.router import router as customers_router
from accounts.router import router as accounts_router

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router=customers_router)
app.include_router(router=accounts_router)

@app.get("/")
def root():
    return "this is the root"
