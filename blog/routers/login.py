from fastapi import Depends, status, HTTPException
from fastapi import APIRouter
from tools import tags, models, jwtToken, schemas
from sqlalchemy.orm import Session
from tools import schemas, hashing
from tools.database import get_db
from datetime import timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    prefix="/login",
    tags=[tags.Tags.login]
)

@router.post("/", status_code=status.HTTP_200_OK)
def login(cradentials: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == cradentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'OOPS! No user Found With Email {cradentials.username}')
    else:
        if not hashing.Hash.verify_password(cradentials.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'OOPS! Incorrect Password')
        else:
            access_token_expires = timedelta(minutes=jwtToken.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = jwtToken.create_access_token(
                data={"sub": user.email}, expires_delta=access_token_expires
            )
            return schemas.Token(access_token=access_token, token_type="bearer")