from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')


class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        else:
            return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, "No tiene permiso para ingresar a este modulo")
        return redirect(self.get_url_redirect())
