from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit omport UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reserve_lazy
from django.shortcuts import get_object_or_404
from .models import AdvUser
from .forms import ChangeUserInfoForm
# Create your views here.
def index (request):
    return render(request, 'main/index.html')

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView):
    template_name='main/login.html'

@login_required #декоратор @login_reqyired -  доступ до сторінки профілю надається тільки зареєстрованим користувачам
def profile(request):
    return render(request, 'main/profile.html')

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

    
class ChangeUserInfoForm (SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_info.html'
    form_class = ChangeUserInfoForm
    succecc_url = reverse_lazy('main:profile')
    success_message = 'Дані змінено'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    def get_object (self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
