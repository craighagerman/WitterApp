from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# To run the app, use the command:
#
# uvicorn main:app --reload --port 8000
