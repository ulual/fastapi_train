from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


# request Get method url: "/" - this is for root.
@app.get("/")
def root():
    return {"message": "Hello World"}




@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return{"new_post": f"title: {payload['title']} content: {payload['content']}"}