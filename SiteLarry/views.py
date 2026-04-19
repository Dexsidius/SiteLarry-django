from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class PortfolioView(TemplateView):
    template_name = "templates/index.html"

    def get(self, request):
        return HttpResponse("Hellow, World")

