from .models import APILog
import json


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the incoming request
        log_entry = APILog.objects.create(
            path=request.path,
            method=request.method,
            request_body=json.dumps(request.data) if request.method == 'POST' else None
        )

        response = self.get_response(request)

        # Log the outgoing response
        log_entry.response_body = response.content.decode()
        log_entry.save()

        return response
