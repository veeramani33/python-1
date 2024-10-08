from pydantic import BaseModel
from typing import List, Optional

class blog(BaseModel):
    title: str
    body: str

class blogBase(blog):
    class Config():
        orm_mode = True 

class user(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    creator: List[blogBase] = []
    class Config():
        orm_mode = True    

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str    

class TokenData(BaseModel):
    email: Optional[str] = None  