from fastapi import APIRouter

from .auth import auth_router
from .post import post_router

router = APIRouter(prefix="/api", tags=["API"])

router.include_router(auth_router)
router.include_router(post_router)

