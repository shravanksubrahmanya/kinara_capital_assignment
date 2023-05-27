from django.views.generic import TemplateView
from django.shortcuts import render

def default_view(request):
    return render(request, 'index.html')

class Homepage(TemplateView):
    template_name='index.html'