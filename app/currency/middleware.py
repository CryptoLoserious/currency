from time import time
from currency.models import RequestResponseLog


class RequestResponseLogTimeItMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()
        print(f'After in middleware {end - start}')

        RequestResponseLog.objects.create(
            path=request.path,
            request_method=request.method,
            time=end - start
        )

        return response
