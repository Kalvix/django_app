from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"

class AboutPage(TemplateView):
    template_name = "about.html"

def homePageView(request):
    return HttpResponse("Hello world")