from fastapi import FastAPI, Query, Path
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, query_param: Optional[str] = None):
    return {"item_id": item_id, "query_param": query_param}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
