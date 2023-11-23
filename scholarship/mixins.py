from django.core.exceptions import PermissionDenied


class JudgesMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Judges').exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ModeratorsMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Moderators').exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
