from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('main/', views.Dog_main.as_view(), name='main'),
    path('ourdog/',views.Our_dog.as_view(), name='ourdog')
]
