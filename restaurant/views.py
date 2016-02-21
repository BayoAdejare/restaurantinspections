from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from restaurant.models import Universe

# Create your views here.
def index(request):
    template = loader.get_template('restaurant/index.html')

    print(Universe.get_univ_hist(Universe,40356018))
    context = {}
    return HttpResponse(template.render(context, request))
