from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Swarup Shah"}

@app.get("/items/users")
def read_item_user():
    return {"item_id": "item"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
def read_parameter(user_id: int, limit:int = 10, sort: Optional[bool] = False):
    if sort:
        return {
            "data": f"This is sorted blogs of user {user_id}",
            "blog langth":limit
        }
    else:
        return {
                "data": f"This is unsorted blogs of user {user_id}",
                "blog langth":limit
            }
class User(BaseModel):
    name: str
    age: int
    sex: Optional[str] = 'male'


@app.post("/user")
def create_user(user: User):
    return {
        'message':'create user',
        'data':user
    }