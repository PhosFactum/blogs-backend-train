from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src import schemas, models
from src.hashing import Hash


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} in not available"
        )
    return user


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update(id: int, request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.Blog.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found"
                            )

    user.update(request.model_dump())
    db.commit()
    return "updated"


def destroy(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    user.delete(synchronize_session=False)
    db.commit()
    return "done"