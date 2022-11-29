from fastapi import FastAPI

from app.routes.system import router as system_router
from app.utils.errors import init_exception_handlers
from app.utils.middleware import init_middleware

app = FastAPI(
    # title=APP_TITLE,
    # description=APP_DESCRIPTION,
    # version=__version__,
)

app.include_router(system_router, tags=["system"])

init_exception_handlers(app)
init_middleware(app)
