from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
