# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:09:30 2022

@author: M01
"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import datetime
import json

app = FastAPI()

class Item(BaseModel):
    DeviceID: str
    # description: Union[str, None] = None
    # price: float
    # tax: Union[float, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = {"date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 
    item_dict.update({"responses": item.dict()})
    with open("result.json", "a+", encoding='utf-8') as f:
        json.dump(item_dict, f, indent=4)
        f.write('\r')
    return item_dict

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    uvicorn.run(app, host=HOST, port=PORT)
    
    
    