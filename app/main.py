from fastapi import FastAPI

from app.utils.errors import init_exception_handlers

from app.routes.system import router as system_router

app = FastAPI(
    # title=APP_TITLE,
    # description=APP_DESCRIPTION,
    # version=__version__,
)

app.include_router(system_router, tags=["system"])

init_exception_handlers(app)
