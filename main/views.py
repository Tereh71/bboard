from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_reqyired


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

@login_reqyired #декоратор @login_reqyired -  доступ до сторінки профілю надається тільки зареєстрованим користувачам
def profile(request):
    return render(request, 'main/profile.html')
