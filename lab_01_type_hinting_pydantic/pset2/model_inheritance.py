"""
Implement Model Inheritance in Pydantic
Benefits: code reutilization, mantainability, extensibility

- Create RoutineBase model: name: str, difficulty: Beginner, Intermediate, Advanced (Enum)
- Create RoutineCreate model: password (at least 8 characters long, regex)
- Create RoutineRead model: id: int. (PROVE IT DOESNT HAS THE PASSWORD )

"""

from typing import Literal
from pydantic import BaseModel, Field, field_validator


class RoutineBase(BaseModel):
    name: str
    difficulty: Literal["Beginner", "Intermediate", "Advanced"]
    

class RoutineCreate(RoutineBase):
    password: str

    @field_validator("password")
    @classmethod
    def correct_password(cls, v: str) -> str:
        if not len(v) >= 8:
            raise ValueError(f"{v} is not a valid password")
        return v
    

class RoutineRead(RoutineBase):
    id: int


RoutineBase(name="Strength", difficulty="Beginner") #good
#RoutineBase(name="Strength", difficulty="Extreme") #bad

RoutineCreate(name="Hypertrophy", difficulty="Intermediate", password="mypass") #good
#RoutineCreate(name="Hypertrophy", difficulty="Beginner", password="mypassword") #bad

print(RoutineRead(name="Skill", difficulty="Advanced", id=5).model_dump()) # shouldnt display password
