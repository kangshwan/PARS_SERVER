from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import generic
from django.core import serializers
from plotly.offline import plot
from plotly.graph_objs import Scatter
from dogfeed.models import Pet,Amount
import json
import requests


# Create your views here.


class Dog_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'dogfeed/main.html'
        json_serializer = serializers.get_serializer("json")()
        # dogs = json_serializer.serialize(Pet.objects.all(), ensure_ascii=False)
        dogs=Pet.objects.all()
        amounts = Amount.objects.all()
        x_data=[]
        y_data=[]
        for dog in dogs:
            print(dog.name)
            amounts=Amount.objects.filter(name=dog)
            for amount in amounts:
                print(amount.name, amount.weight, amount.time)
                x_data.append(amount.time)
                y_data.append(amount.weight)
                
        plot_div = plot([Scatter(x=x_data, y=y_data,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='green')],
                    output_type='div',include_plotlyjs=False)
        return render(request, template_name, context={'plot_div': plot_div, 'dog_names': dogs})
    @csrf_exempt
    def post(self,request):
        if request.method == 'POST':
            received_json_data=json.loads(request.body)
            print(received_json_data['data']['time'])
            Amount.objects.create(name=Pet.objects.get(name='초코'),weight=400, time="2020-06-18 07:00:00.000000")
            # amountData = Amount.objects.filter(name__name=received_json_data['data']['name'])
            # amountData.weight=300
            # amountData.time="2020-06-18 07:00:00.000000"
            # amountData.save()
            
            return HttpResponse('it was post request: '+str(received_json_data))
        return HttpResponse('it was GET request')
class Our_dog(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name='dogfeed/ourdog.html'
        return render(request, template_name)