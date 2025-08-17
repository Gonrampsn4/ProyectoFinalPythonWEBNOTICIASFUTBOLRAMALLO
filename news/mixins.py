
from django.core.exceptions import PermissionDenied

class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.is_authenticated or obj.author != request.user:
            raise PermissionDenied("No tienes permisos para modificar este objeto.")
        return super().dispatch(request, *args, **kwargs)
