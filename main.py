from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "안녕, Jay"}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search")
def search(q: str, limit: int = 10):
    return{"q": q, "limit": limit}

@app.get("/users/{user_id}/items")
def user_items(user_id: int, q: str | None = None ):
    return {"user_id": user_id, "q": q}