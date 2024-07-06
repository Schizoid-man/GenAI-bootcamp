from fastapi import FastAPI
from app.models import get_similar_words
from app.schemas import WordRequest

app = FastAPI()

@app.post("/similar-words/")
async def similar_words(request: WordRequest):
    return get_similar_words(request.word)
