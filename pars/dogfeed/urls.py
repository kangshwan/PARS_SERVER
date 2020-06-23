from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Main_dog.as_view()),
    path('home/', views.Main_dog.as_view(), name='home'),
    path('ourdog/', views.Our_dog.as_view(), name='ourdog'),
    path('viewdog/',views.View_dog.as_view(), name='viewdog')
]
