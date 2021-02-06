from typing import Optional
from fastapi import FastAPI
from fastapi import Request
import uvicorn as uv
import eventkit as ev

app = FastAPI()
gh_event = ev.Event()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# http post http://localhost:5000/webhooks/github hi=there --json
@app.post("/webhooks/github")
async def github_webhook(req: Request):
    gh_event.emit(await req.json())
    return "OK"


def process_github(json):
    print(json["hi"])


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


def main():
    global gh_event
    gh_event += process_github
    uv.run("badges.main:app", host="127.0.0.1", port=5000, log_level="info")
