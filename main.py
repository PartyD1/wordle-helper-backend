from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Wordle helper backend running"};

@app.post("/analyze")
def analyze(guesses: list[str]):
    return {"remaining_words": 231}