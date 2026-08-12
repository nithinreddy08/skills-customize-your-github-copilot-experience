# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API in Python using FastAPI, create endpoints, validate request data, and return JSON responses for a simple application.

## 📝 Tasks

### 🛠️ Create the API app

#### Description
Set up a FastAPI application that exposes basic endpoints for managing a collection of items or tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define at least one GET endpoint that returns JSON data
- Define at least one POST endpoint that accepts input data
- Return clear JSON responses for successful requests
- Run the app locally with Uvicorn or FastAPI's development server

### 🛠️ Add request validation and data models

#### Description
Use Pydantic models to validate incoming data and structure your API responses.

#### Requirements
Completed program should:

- Define a data model for the resource being managed
- Validate required fields such as `title`, `description`, or `completed`
- Reject invalid input with useful validation errors
- Store data in memory for the current session
- Demonstrate how to fetch all items and add a new item via API calls

### 🛠️ Build a practical API flow

#### Description
Create a simple API for managing a list of tasks, notes, or products and make sure the endpoints behave like a real REST API.

#### Requirements
Completed program should:

- Support listing all resources with a `GET` request
- Support creating a new resource with a `POST` request
- Include a unique identifier for each item
- Return the created item in the response body
- Provide example usage such as:

```python
@app.get("/items")
def get_items():
    return items
```

```http
POST /items
{
  "title": "Write API assignment",
  "description": "Finish the FastAPI exercise",
  "completed": false
}
```
