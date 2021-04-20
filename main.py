from fastapi import FastAPI

app=FastAPI()
@app.get("/") # dekorator
def root():
    return {"message": "Hello world"}
