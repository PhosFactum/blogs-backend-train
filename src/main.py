from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database import engine, get_db
from src.hashing import Hash
from . import schemas
from . import models
from .routers import blog
from .routers import user


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)
