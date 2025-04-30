from fastapi import FastAPI

from .routes import router

app = FastAPI(title="To-Do List API", version="0.1")

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "API is working"}
