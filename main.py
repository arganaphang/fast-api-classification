from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()
modelML = pickle.load(open("./model/model.pkl", "rb"))

category = {0: "Tidak Bagus", 1: "Bagus"}


class Item(BaseModel):
    nilai: int
    homepage: int
    modul_perkuliahan: int
    forum: int
    tugas: int
    kuis: int
    uts: int
    uas: int


@app.get("/")
def index():
    return {"message": "OK"}


@app.post("/predict")
async def say(item: Item):
    predict = modelML.predict(
        [
            [
                item.nilai,
                item.homepage,
                item.modul_perkuliahan,
                item.forum,
                item.tugas,
                item.kuis,
                item.uts,
                item.uas,
            ]
        ]
    )
    return {"message": category[predict[0]]}
