from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database (list)
db = []

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    db.append(item)
    return {"message": "Item created successfully!", "item": item}

@app.get("/items/")
def get_items():
    return db

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return {"message": "Item updated successfully!", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = db.pop(item_id)
    return {"message": "Item deleted successfully!", "item": deleted_item}
