from fastapi import FastAPI
from api.database import create_db_and_tables
from api.public import api as public_api


def create_app(settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
    )

    @app.on_event("startup")
    def on_starup():
        create_db_and_tables()
        
    @app.get("/ping")
    def pong():
        return {"ping": "pong!"}

    app.include_router(public_api)

    return app
