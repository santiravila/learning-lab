"""
Implement serialization and aliases in Pydantic
Benefits: better interface contracts (translation between outside (JS/JSON) and inside (Python)), data masking

- Create ExerciseAPI Pydantic model
- fields: exercise_name, muscle_group, calories_per_minutes
- map:
exercise_name <-> exerciseName
muscle_group <-> muscleGroup
calories_per_minute <-> kcalPerMin
- JSON: {"exerciseName": "Burpees", "muscleGroup": "Full Body", "kcalPerMin": 11.5}
* print python object showing snake_case
* export back to JSON using the aliases
"""


from pydantic import BaseModel, Field


class ExerciseAPI(BaseModel):
    exercise_name: str = Field(alias="exerciseName")
    muscle_group: str = Field(alias="muscleGroup")
    calories_per_minute: float = Field(alias="kcalPerMin")


from_json = {"exerciseName": "Burpees", "muscleGroup": "Full Body", "kcalPerMin": 11.5}
exercise = ExerciseAPI(**from_json)
print(exercise)

to_json = exercise.model_dump(by_alias=True)
print(to_json)