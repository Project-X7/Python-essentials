from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/users")
def get_users():
    return {"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}

@app.post("/create_user")
def create_user(user: User):
    return {"message": f"User {user.name} created successfully!"}