from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/webhooks/github")
def github_webhook():
    # TODO: Create an event.
    return "OK"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


def main():
    uvicorn.run("badges.main:app", host="127.0.0.1", port=5000, log_level="info")
