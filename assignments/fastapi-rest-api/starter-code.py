from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Item(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Create a GET endpoint to return all items
# TODO: Create a POST endpoint to add a new item
# TODO: Validate item data using the Item model
# TODO: Return the created item in the response
