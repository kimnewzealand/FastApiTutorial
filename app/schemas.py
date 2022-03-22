from pydantic import BaseModel,EmailStr


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str