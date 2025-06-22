import sentry_sdk


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class SentryUserIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        with sentry_sdk.configure_scope() as scope:
            ip_address = get_client_ip(request)
            scope.set_user(
                {
                    "ip_address": ip_address,
                }
            )
        response = self.get_response(request)
        return response
