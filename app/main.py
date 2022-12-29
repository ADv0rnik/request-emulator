import uvicorn
from fastapi import FastAPI
from app.config import settings, Settings


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main.py",
        port=int(settings.PROJECT_PORT),
        host=settings.PROJECT_HOST,
        reload=True
    )
