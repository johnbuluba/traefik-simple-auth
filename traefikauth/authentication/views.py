from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, redirect_to_login
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
import logging

from django.views import View

logger = logging.getLogger(__name__)


class TraefikLoginView(LoginView):

    def get(self, request, *args, **kwargs):
        logger.debug(request.META)
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        logger.debug(form.request.META)
        res = super().form_invalid(form)
        res.status_code = 401
        return res

    def get_redirect_url(self):
        return self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )


class AuthView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = 'next'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=200)

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())
        if "HTTP_X_FORWARDED_HOST" in self.request.META and "HTTP_X_FORWARDED_PROTO" in self.request.META:
            redirect_url = "{}://{}".format(self.request.META["HTTP_X_FORWARDED_PROTO"], self.request.META["HTTP_X_FORWARDED_HOST"])
            return redirect_to_login(redirect_url, self.get_login_url(), self.get_redirect_field_name())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
