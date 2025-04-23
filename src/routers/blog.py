from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.repository import blog
from src.database import get_db
from src import schemas, oauth2


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


# Handlers
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db),
                  current_user: schemas.User =
                  Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db),
             current_user: schemas.User =
             Depends(oauth2.get_current_user)):
    return blog.get(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def post_blog(request: schemas.Blog, db: Session = Depends(get_db),
              current_user: schemas.User =
              Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User =
                Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db),
                current_user: schemas.User =
                Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)