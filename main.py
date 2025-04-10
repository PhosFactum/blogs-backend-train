from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "Man!"}


@app.get("/page")
def get_page(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published pages from the db"}
    else:
        return {"data": f"{limit} pages from the db"}


@app.get("/about")
def get_about():
    return {"data": "about page"}


@app.get("/page/unpublished")
def get_unpublished():
    return {"data": "all unpublished pages"}


@app.get("/page/{id}")
def get_page(id: int):
    return {"data": id}


@app.get("/page/{id}/info")
def get_page_info(id, limit=10):
    return {"data": {"1", "2"}}


class Page(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/page")
def create_page(page: Page):
    return {"data": f"Page is created with title as {page.title}"}
