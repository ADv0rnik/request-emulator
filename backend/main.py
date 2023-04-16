import logging.config

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import Settings
from app.core.config import LOGGING_CONFIG
from app.api.api import api_router


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("bookshelf")


def start_application(config: Settings):
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description="Book store emulator",
        openapi_url=f"{settings.API_V1_STR}/bookshelf.json",
        docs_url=f"{settings.API_V1_STR}/docs"
    )
    return application


settings = Settings()

app = start_application(settings)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=int(settings.PROJECT_PORT),
        host=settings.PROJECT_HOST,
        reload=True
    )
    logger.info("Start application")
