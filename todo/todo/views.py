from django.shortcuts import render
from django.views import *


def MainPageView(request):
    template_name = 'site_main_page.html'
    return render(request, template_name=template_name)
