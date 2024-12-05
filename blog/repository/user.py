from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from tools import schemas, models, hashing

def get_user(id: int, db: Session):
    if id == 0:
        users = db.query(models.User).all()
        return users
    else:
        blog = db.query(models.User).filter(models.User.id == id).first()
        if not blog:
            # response.status_code = status.HTTP_404_NOT_FOUND
            # return {'Message': 'Blog Not Found'}
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User not found for the id {id}')
        return blog

def create_user(user: schemas.User, db: Session):
    new_user = models.User(name = user.name,email = user.email, hashed_password = hashing.Hash.hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        'message':'Created user',
        'data':{'name': user.name,
                'email': user.email}
    }