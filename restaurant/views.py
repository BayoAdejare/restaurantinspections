from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('restaurant/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
