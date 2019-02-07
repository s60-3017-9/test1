from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>/',views.show,name='show'),
    path('input/',views.input,name='input')
]