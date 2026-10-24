from fastapi import FastAPI
from customer.router import router


app = FastAPI()
app.include_router(router=router)

@app.get("/")
def root():
    return "this is the root"
