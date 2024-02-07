from fastapi import FastAPI
from typing import List
import pickle
from pydantic import BaseModel

app = FastAPI()
modelML = pickle.load(open("./model/model.pkl", "rb"))

category = {0: "Tidak Bagus", 1: "Bagus"}


class Item(BaseModel):
    data: List[int]


@app.get("/")
def index():
    return {"message": "OK"}


@app.post("/predict")
async def say(item: Item):
    predict = modelML.predict([item.data])
    return {"message": category[predict[0]]}
