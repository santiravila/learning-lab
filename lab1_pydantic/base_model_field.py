"""
Type Hinting / Pydantic lab
"""


from pydantic import BaseModel, Field


class WorkoutInput(BaseModel):
    exercise_name: str
    duration_minutes: int = Field(gt=0) # gt = greather than
    intensity: float = Field(ge=0, le=1) # ge/le = greater/lesser or equal than


class WorkoutResult(BaseModel):
    exercise: str
    calories: float


def calculate_calories_pydantic(workout_input: WorkoutInput) -> WorkoutResult:
    calories = workout_input.duration_minutes * workout_input.intensity * 5
    return WorkoutResult(exercise=workout_input.exercise_name, calories=calories)


# dict[X, Y | Z]. X: key datatype, Y | Z: values datatypes
def calculate_calories(exercise_name: str, duration_minutes: int, intensity: float) -> dict[str, str | float]:
    calories = duration_minutes * intensity * 5 
    return {"exercise": exercise_name, "calories": calories}


# X | None for optional parameters
def get_workout(workout_id: int, user_id: int | None = None) -> dict[str, str | int]:
    return {"test": 1}


def main():
    print(calculate_calories("pushups", 5, 0.5))
    get_workout(1)

    good_workout = WorkoutInput(exercise_name="pushups", duration_minutes=5, intensity=0.5)
    calories_good = calculate_calories_pydantic(good_workout)
    print(calories_good)
    print(calories_good.model_dump())

    bad_workout = WorkoutInput(exercise_name="plank", duration_minutes=-1, intensity=2)
    calories_bad = calculate_calories_pydantic(bad_workout)
    print(calories_bad)
    print(calories_bad.model_dump())



main()