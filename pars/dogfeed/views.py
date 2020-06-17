from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core import serializers
from plotly.offline import plot
from plotly.graph_objs import Scatter
from dogfeed.models import Pet
# Create your views here.
def index(request):
    x_data=[0,1,2,3]
    y_data=[x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')
    return HttpResponse("Hello, world. You're at the dogfeed index!")

class Dog_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'dogfeed/main.html'
        json_serializer = serializers.get_serializer("json")()
        # dogs = json_serializer.serialize(Pet.objects.all(), ensure_ascii=False)
        dogs=Pet.objects.all()
        x_data=[0,1,2,3]
        y_data=[x**2 for x in x_data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='green')],
                    output_type='div',include_plotlyjs=False)
        return render(request, template_name, context={'plot_div': plot_div, 'dog_names': dogs})
