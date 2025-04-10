from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def baseFunc():
    return {"data": {"name": "Mike"}}


@app.get("/about")
def about():
    return {"data": "about page"}
