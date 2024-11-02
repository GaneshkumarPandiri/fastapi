from pydantic import BaseModel,EmailStr,conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    # rating:Optional[int] = None

class CreatePosts(PostBase):
    pass
class UpdatePosts(PostBase):
    pass

class UserResponse(BaseModel):
    id : int
    email : str
    created_at : datetime
    class config:
        orm_mode = True

class PostsRespopnse(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserResponse

    class config:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password :str



class UsersLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token : str
    token_type :str

class TokenData(BaseModel):
    id : Optional[int] = None

class CreateVote(BaseModel):
    post_id : int
    dir : int
