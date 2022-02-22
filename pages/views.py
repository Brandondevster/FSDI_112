from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HOME(TemplateView):
    template_name = "index.html"

class ABOUT(TemplateView):
    template_name = "about.html"