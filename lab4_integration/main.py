from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

# a User DTO
class User(BaseModel):
    username: str = Field(alias="userName") 
    role: str 
    is_active: bool = Field(alias="isActive")


# pretends to be a database call
def current_user():
    user_data = {
        "userName": "john doe",
        "role": "admin",
        "isActive": "yes"
    }

    return user_data


app = FastAPI()


@app.get("/whoami", response_model=User)
def who_am_i(user: dict = Depends(current_user)):
    return user