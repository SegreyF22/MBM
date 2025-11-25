# from django.views.generic import TemplateView
#
#
# class IndexView(TemplateView):
#     template_name = 'main/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'MBM - Главная'
#         context['content'] = 'Книжный интернет магазин MBM (Myski Books Magazine)'
#         return context
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('About page')