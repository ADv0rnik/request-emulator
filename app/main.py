import uvicorn
import tasks
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config import settings, Settings


def start_application(config: Settings):
    app = FastAPI(
        debug=True,
        version=config.PROJECT_VERSION,
        title=config.PROJECT_NAME
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("start_app", tasks.create_start_app_handler(app))
    app.add_event_handler("stop_app", tasks.create_stop_app_handler(app))
    # add routes here

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
