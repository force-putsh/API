from fastapi import FastAPI

app = FastAPI()

@app.get("/goodbye")
def goodbye():
    return {"message": "Goodbye from Service 2"}
