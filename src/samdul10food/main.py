# src/samdul10food/main.py

from typing import Union
from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return { "Hello": "world!", "this is": "src/samdul10/main.py" }

@app.get("/food")
def food(name: str):
    # implement access time save
    # save name,time : ~/code/data/good.csv
    return { "food": name, "time": "2024-09-12" }
