from enum import Enum
from typing import Literal

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


class Subjects(str, Enum):
    math = "math"
    programming = "programming"
    circuits = "circuits"


class Notebook(BaseModel):
    id: int
    subject_name: Subjects
    notes: str


class MockDB:
    def get_data(self):
        return [
            Notebook(id=1, subject_name=Subjects.math, notes="e=m2"), 
            Notebook(id=2, subject_name=Subjects.programming, notes="<code>"), 
            Notebook(id=3, subject_name=Subjects.circuits, notes="bip bop"), 
        ]


def get_db() -> MockDB:
    return MockDB()


def list_notebooks(
    sort_by: Literal["id", "subject_name"] | None = None,
    db: MockDB = Depends(get_db)
    ) -> list[Notebook]:

    notebooks = db.get_data()
    
    if sort_by == "id":
        notebooks.sort(key=lambda n: n.id)
    elif sort_by == "subject_name":
        notebooks.sort(key=lambda n: n.subject_name)


    return notebooks


@app.get("/")
def root():
    return {"message": "No notebooks yet"}


@app.get("/notebooks/", response_model=list[Notebook])
def get_all_notebooks(
    notebooks: list[Notebook] = Depends(list_notebooks),
):
    return notebooks


@app.get("/notebooks/{notebook_id}", response_model=Notebook)
def notebooks(
    notebook_id: int, 
    notebooks: list[Notebook] = Depends(list_notebooks),
):
    for notebook in notebooks:
        if notebook.id == notebook_id:
            return notebook
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Notebook not found"
    )
    
        




