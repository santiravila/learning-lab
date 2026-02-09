from fastapi import FastAPI


app = FastAPI()


@app.get("/files")
def files():
    return {"files": "some files in the directory"}


@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
