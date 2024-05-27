from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return { 
        "data": 'Welcome Home Page'
    }


@app.get('/blog')
def index(limit=10, published:bool = True, sort: Optional[str] = None):
    if published:
        return { 
            'data': f'{limit} published blogs from the DB'
        }
    else:
        return {
            'data': f'{limit} blogs from the DB'
        }


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'All unpublished blogs'
    }


@app.get('/blog/{id}')
def show(id:int):
    return {
        'data': id
    }

@app.get('/blog/{id}/comments')
def comments(id:int, limit = 10):
    return {
        'comments': {
            '1', '2'
        }
    }


class Blog(BaseModel):
    title: str
    body: str | None = None
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {
        'data' : f'Blog is created with {request.title}'
    }