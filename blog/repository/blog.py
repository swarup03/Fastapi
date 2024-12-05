from fastapi import HTTPException, status
from tools import schemas, models
from sqlalchemy.orm import Session



def create_blog(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title = blog.title, description = blog.description, owner_id = 2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        'message':'create Blog',
        'data':blog
    }

def get_blog(id: int, db: Session):
    if id == 0:
        blogs = db.query(models.Blog).all()
        return blogs
    else:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            # response.status_code = status.HTTP_404_NOT_FOUND
            # return {'Message': 'Blog Not Found'}
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog not found for the id {id}')
        return blog
    
def delete_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog not found for the id {id}')
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {
            'message':f'Blog removed of id {id}'
        }

def update_blog(id: int, blog_upd: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog not found for the id {id}')
    else:
        print(blog.first())
        print(blog_upd)
        blog.update(blog_upd.dict())
        db.commit()
        return {
            'message':f'Blog updated of id {id}'
        }