import logging

from django.http import HttpRequest, JsonResponse

logger = logging.getLogger("async_logstash_memory_leak")


def ok_view(request: HttpRequest):
    logger.info("test")
    return JsonResponse({
        "status": "ok"
    })
