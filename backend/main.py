import uvicorn
from fastapi import FastAPI
from core.config import Settings, settings


def start_application(config: Settings) -> FastAPI:
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        openapi_url=f"{config.API_URL}/request_emulator.json"
    )
    return application


app = start_application(settings)


@app.get('/')
def get_index():
    return {"Hello": "world"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=int(settings.PROJECT_PORT),
        host=settings.PROJECT_HOST,
        reload=True
    )
