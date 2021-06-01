from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

### Tony's running code for users

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str


blognew = []


@app.post('/blog')
def create_blog(blog: Blog):
    blognew.append(blog)
    return {'data': f'Blog is created with title as {blog.title}'}


@app.get('/blog')
def get_blog():
    return blognew
