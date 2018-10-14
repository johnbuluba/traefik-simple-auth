from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import login
# Create your views here.


class LoginView(LoginView):

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponse(status=200)

    def form_invalid(self, form):
        res = super().form_invalid(form)
        res.status_code = 401
        return res
