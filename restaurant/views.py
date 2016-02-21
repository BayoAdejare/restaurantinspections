from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from restaurant.models import Universe
from django.shortcuts import render_to_response
import json as simplejson

# Create your views here.
def index(request):
    template = loader.get_template('restaurant/index.html')
    univ = Universe()
    univ_list = Universe.get_univ_ids(univ)
    my_list = []
    count = 0;
    for row in univ_list:
        if count < 10:
            my_list.append(list(row))
            count += 1
        else:
            break
    print(my_list[0][0])
    json_list = simplejson.dumps(my_list)
    return render_to_response('C:\\Users\\Anthony\\PycharmProjects\\restaurantinspections\\restaurant\\templates\\restaurant\\index.html', {'m_list': my_list})
