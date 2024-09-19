from fastapi import Depends, status
from typing import List
from fastapi import APIRouter
from tools import tags
from sqlalchemy.orm import Session
from tools import schemas
from tools.database import get_db
from repository import user as usr


router = APIRouter(
    prefix="/user",
    tags=[tags.Tags.users]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return usr.create_user(user, db)

@router.get("/users", response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db)):
    return usr.get_user(id= 0, db = db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return usr.get_user(id, db)