"""
Requirements:
- Implement a Pydantic model named WorkoutInput  
- Validate that intensity cant be > 0.7 on rest days
- Normally intensity: [0, 1]
- WorkoutInput has exercise_name, duration_minutes
- Raise a ValueError("message") if validation fails

LEARNED: Custom validators (model_validator) for cross-field validation
"""


from pydantic import BaseModel, Field, model_validator


class WorkoutInput(BaseModel):
    exercise_name: str
    duration_minutes: int = Field(gt=0)
    intensity: float = Field(ge=0, le=1)
    is_rest_day: bool

    # cross-field validation with Validation Info
    @model_validator(mode="after")
    def check_rest_day_intensity(self):
        if self.is_rest_day and self.intensity > 0.7:
            raise ValueError("Intensity cant be greater than 0.7 on rest days")
        return self


WorkoutInput(exercise_name="Yoga", duration_minutes=30, intensity=0.5, is_rest_day=True)   # Should work
WorkoutInput(exercise_name="Sprints", duration_minutes=20, intensity=0.9, is_rest_day=True) # Should fail
