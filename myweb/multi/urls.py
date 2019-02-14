from django.urls import path
from . import views

app_name = 'multiply'
urlpatterns = [
    path('<int:number>/',views.show,name='show'),

    path('input/',views.input,name='input'),

    path('results/',views.results,name='results'),




]