from django.core.exceptions import PermissionDenied


class JudgesMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='judges').exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ModeratorsMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='moderators').exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
