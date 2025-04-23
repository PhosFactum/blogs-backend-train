from typing import List, Optional

from pydantic import BaseModel


# Basic models
class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


# For representation
class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True


# Login and JWT
class Login(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None