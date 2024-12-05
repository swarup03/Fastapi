from fastapi import FastAPI
from tools import models
from tools.database import engine
from routers import blog, demo, user, login

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(login.router)
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(demo.router)