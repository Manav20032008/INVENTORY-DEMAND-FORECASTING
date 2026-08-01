import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from backend.logging.logger import get_logger

logger = get_logger()
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        start = time.perf_counter()

        logger.info("request_started method=%s path=%s request_id=%s",
                    request.method,request.url.path,request_id,)

        try:
            response = await call_next(request)
        except Exception:
            logger.exception("request_failed method=%s path=%s request_id=%s",
                             request.method,request.url.path,request_id,)
            raise

        duration_ms = (time.perf_counter() - start) * 1000

        logger.info("request_completed method=%s path=%s status=%s duration_ms=%.2f request_id=%s",
                    request.method,request.url.path,response.status_code,duration_ms,request_id,)
        response.headers["x_request_id"] = request_id

        
        return response
