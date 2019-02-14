from django.urls import path
from . import views

app_name = 'multiply'
urlpatterns = [
    path('<int:number>/',views.show,name='show'),

    path('input/',views.input,name='input'),

    path('results/',views.results,name='results'),

    path('results-by-count/',views.results_by_count,name='results_count'),

    path('results-by-num/',views.results_by_num,name='results_num')





]