from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from database import engine, SessionLocal
from sqlalchemy.orm import Session

import schemas, models


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### Endpoints ###

# Blog handlers
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def post_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"done"}


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found"
        )
    blog.update(request)
    db.commit()
    return "updated"


@app.get("/blog", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not available"
        )
    return blog


# Users handlers
@app.post("/user")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user", response_model=List[schemas.ShowBlog])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
