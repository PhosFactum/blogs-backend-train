from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"data": "blog list"}


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
def get_page_info(id):
    return {"data": {"1", "2"}}
