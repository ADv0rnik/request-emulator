import uvicorn
from fastapi import FastAPI
from config import settings, Settings


def start_application(config: Settings):
    app = FastAPI(
        debug=True,
        version=config.PROJECT_VERSION,
        title=config.PROJECT_NAME
    )
    return app


application = start_application(settings)


@application.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:application",
        port=int(settings.PROJECT_PORT),
        host=settings.PROJECT_HOST,
        reload=True
    )
