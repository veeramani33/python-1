from typing import List
from .. import schemas, database, oauth2
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix = '/blog',
    tags=['blogs']
)


@router.get('/', response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.user = Depends(oauth2.get_current_user)):
    return  blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schemas.blog, db: Session = Depends(database.get_db), current_user: schemas.user = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)


@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session=Depends(database.get_db), current_user: schemas.user = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id, request: schemas.blog, db:Session=Depends(database.get_db), current_user: schemas.user = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)

@router.get('/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id, db: Session=Depends(database.get_db), current_user: schemas.user = Depends(oauth2.get_current_user)):
    return blog.get_blog(id, db)

