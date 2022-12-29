from fastapi import FastAPI, Query, Body

app = FastAPI()

@app.post("/aueu/")
def displayPostedQueu(body: dict = Body(None)):
    print(body["message"])
    return null