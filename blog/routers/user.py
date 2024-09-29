from typing import List
from .. import schemas, database, models, hashing
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix = '/user',
    tags=['users']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schemas.user, db: Session = Depends(database.get_db)):
    return user.create_user(request, db)


@router.get('/{id}',response_model = schemas.ShowUser, status_code=200)
def get_user(id, db: Session = Depends(database.get_db)):
    return user.get_user(id, db)

@router.get('/',response_model = List[schemas.ShowUser])
def get_all(db: Session = Depends(database.get_db)):
    return user.get_all(db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_user(id, db: Session = Depends(database.get_db)):
    return delete_user(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_user(id, request: schemas.user, db: Session = Depends(database.get_db)):
    return user.update_user(id,request,db)