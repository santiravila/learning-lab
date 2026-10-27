from fastapi import FastAPI
from infrastructure.database import Base, engine
from customer.router import router

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router=router)

@app.get("/")
def root():
    return "this is the root"
