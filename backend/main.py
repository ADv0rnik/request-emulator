import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.core.config import Settings, settings
from app.api.routes import router


def start_application(config: Settings) -> FastAPI:
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        openapi_url=f"{config.API_URL}/request_emulator.json"
    )
    return application


app = start_application(settings)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix=settings.API_URL)
api_router.include_router(router)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=int(settings.PROJECT_PORT),
        host=settings.PROJECT_HOST,
        reload=True
    )
