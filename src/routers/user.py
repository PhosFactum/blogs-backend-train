from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.repository import user
from src import schemas


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/", response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=schemas.ShowUser)
def post_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    return user.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.destroy(id, db)