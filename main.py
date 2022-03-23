from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#order of the post matters if the url is the same.

#validate type of the model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# request Get method url: "/"
# to restart in terminal: uvicorn main:app --reload

@app.get('/')
async def root():
    return{'message': 'welcome to my api!!!!!'}

@app.get('/posts')
def get_posts():
    return {"data":"This is your posts"}

@app.post('/createposts')
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "new post"}

#title str, content str