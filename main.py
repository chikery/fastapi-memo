from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MemoCreate(BaseModel):   # 보낼 때 양식
    text: str

class Memo(BaseModel):         # 돌려줄 때 양식
    id: int
    text: str

@app.get("/hello")
def hello():
    return {"message": "안녕, Jay"}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

MEMOS = [
    {"id": 1, "text": "회의 자료 준비"},
    {"id": 2, "text": "SQLD 1과목 복습"},
    {"id": 3, "text": "회의록 정리"},
    {"id": 4, "text": "FastAPI 쿼리 매개변수"},
    {"id": 5, "text": "주간 회의"},
]

@app.get("/search")
def search(q: str, limit: int = 10):
    found = [m for m in MEMOS if q in m["text"]]   # q가 들어간 메모만 고르기
    return found[:limit]                           # 앞에서 limit개만

@app.get("/users/{user_id}/items")
def user_items(user_id: int, q: str | None = None ):
    return {"user_id": user_id, "q": q}

@app.post("/memos", status_code=201)
def create_memo(memo: MemoCreate) -> Memo:
    new = {"id": len(MEMOS) + 1, "text": memo.text}   # 서버가 번호를 붙임
    MEMOS.append(new)                                 # 리스트에 저장
    return new

@app.get("/memos")
def list_memos() -> list[Memo]:
    return MEMOS