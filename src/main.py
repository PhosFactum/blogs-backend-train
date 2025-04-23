from fastapi import FastAPI
from src.database import engine

from src.routers import blog, user, authentication
from src import models


app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)


models.Base.metadata.create_all(engine)