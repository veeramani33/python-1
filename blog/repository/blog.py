from .. import models, schemas
from fastapi import status, HTTPException
from sqlalchemy.orm import Session 

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id )
    if not blog.first():
        raise HTTPException(satus_code = status.HTTP_404_NOT_FOUND, detail = f'{id}- id not found')
    blog.delete(synchronize_session = False)
    db.commit()
    return  'done'

def update_blog(id: int, request : schemas.blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(satus_code = status.HTTP_404_NOT_FOUND, detail = f'{id}- id not found')
    blog.update(request)
    db.commit()
    return 'updated'

def get_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f'id - {id} Not available' )
    
    return blog
