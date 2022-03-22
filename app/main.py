from http.client import HTTPException
from typing import Optional
from fastapi import Depends, FastAPI,  status
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import engine
from sqlalchemy.orm import Session
from . import models, schemas
from . database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_posts(db: Session = Depends(get_db), limit: int = 10, search: Optional[str] = ""):
    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)).limit(limit).all()
    print(limit)
    return posts


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    while True:
        try:
            posts = db.query(models.Post).all()
            print("get is successful")
            break
        except Exception as error:
            print("get failed")

    return posts


@ app.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.Post):
    return post


@ app.get("/posts/{id}")
def get_posts(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'your post has not been found')

    return {"data": f'your post {id} is {post}'}


@ app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    while True:
        try:
            new_user = models.User(**user.dict())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            print("new user is successful")
            break
        except Exception as error:
            print("new user failed", error)
    return new_user
