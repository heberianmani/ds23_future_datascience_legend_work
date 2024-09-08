from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str

#Annotations
@app.get("/welcome")
def helloworld():
    return "Hello I am learning FastAPI with Get Method in Manikandan Thiagarajan Session"

@app.post("/hi")
def helloworld():
    return "Hello I am learning FastAPI with Post Method"

@app.get("/person/{person}")
def great_user_get(person):
    return {"Hi Welcome ": person}

@app.post("/person/")
def great_user_post(data: InputData):
    return {"Hi Welcome ": data.name}