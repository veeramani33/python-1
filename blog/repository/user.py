from .. import models, hashing, schemas
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

def get_all(db: Session):
    return db.query(models.User).all()

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f'id - {id} Not available' )
    return user

def create_user(request: schemas.user, db: Session):
    new_user = models.User(name= request.name, email= request.email, password= hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(id: int, request: schemas.user, db: Session):
    find_user = db.query(models.User).filter(models.User.id == id)
    if not find_user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f'id - {id} Not available' )
    find_user.update(name= request.name, email= request.email, password= hashing.Hash.bcrypt(request.password))
    db.commit()
    return 'User updated'   

def delete_user(id: int, db: Session):
    find_user = db.query(models.User).filter(models.User.id == id)
    if not find_user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f'id - {id} Not available' )
    find_user.delete(synchronize_session = False)
    db.commit()
    return 'user deleted'