from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
shared_data = {"card_index": None}

class Card(BaseModel):
    index: int

@app.post("/send_card")
def send_card(card: Card):
    shared_data["card_index"] = card.index
    return {"status": "card received", "index": card.index}

@app.get("/get_card")
def get_card():
    return {"index": shared_data["card_index"]}
