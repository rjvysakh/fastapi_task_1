from fastapi.routing import APIRouter

from fastapi_task_2.web.api import authentication, document, monitoring


api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(authentication.router, prefix="/auth", tags=["auth"])
api_router.include_router(document.router, prefix="/document", tags=["document"])
