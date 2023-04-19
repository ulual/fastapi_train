from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#Validate the entry of a post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None




# request Get method url: "/" - this is for root.
@app.get("/")
def root():
    return {"message": "Hello World"}



# To look at a post
@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

# To create a post
@app.post("/createposts")
def create_posts(new_posts: Post):
    print(new_posts)
    print(new_posts.dict())
    return{"data": "new post"}
# title str, content str