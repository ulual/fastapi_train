from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

#Validate the entry of a post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
    "title": "favorite food", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p ["id"] == id:
            return p

# request Get method url: "/" - this is for root.
@app.get("/")
def root():
    return {"message": "Hello World"}

# To look at a post
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# To create a post
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return{"data": post_dict}


#id is the path parameter
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = 404
    return {"post_detail": post}



