from typing import Optional
from fastapi import APIRouter
from tools import tags

router = APIRouter(
    prefix="/demo",
    tags=[tags.Tags.demo]
)

@router.get("/")
def read_root():
    return {"Hello": "Swarup Shah"}

@router.get("/items/users")
def read_item_user():
    return {"item_id": "item"}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@router.get("/users/{user_id}")
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
