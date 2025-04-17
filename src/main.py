from fastapi import FastAPI
from src.database import engine

from src.routers import blog
from src.routers import user
from src import models


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)
