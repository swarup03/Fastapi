from fastapi import Depends, status
from typing import List, Annotated
from fastapi import APIRouter
from tools import tags, jwtToken
from sqlalchemy.orm import Session
from tools import schemas
from tools.database import get_db
from repository import blog as blg

router = APIRouter(
    prefix="/blog",
    tags=[tags.Tags.blogs]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    return blg.create_blog(blog,db)

@router.get("/blogs", response_model=List[schemas.ShowBlog])
def get_blogs( current_user: Annotated[schemas.User, Depends(jwtToken.get_current_active_user)], db: Session = Depends(get_db),):
    return blg.get_blog(id=0, db=db)

@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog(id, db: Session = Depends(get_db)):
    return blg.get_blog(id=id, db=db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    return blg.delete_blog(id, db)
    
@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog_upd: schemas.Blog, db: Session = Depends(get_db)):
    return blg.update_blog(id, blog_upd, db)