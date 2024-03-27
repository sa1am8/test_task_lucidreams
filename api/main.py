import time

from database import get_engine
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from logger import log
from router import router
from starlette.middleware.base import BaseHTTPMiddleware

engine = get_engine()

app = FastAPI()
app.include_router(router)


class SizeLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        if len(body) > 1_000_000:  # 1 MB
            raise HTTPException(status_code=413, detail="Payload too large")
        return await call_next(request)


app.add_middleware(SizeLimitMiddleware)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    log(log.INFO, "Time estimated - [%s]", process_time)
    return response


print("done")
