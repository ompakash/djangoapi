from django.urls import path
from . import views
urlpatterns = [
    path("",  views.pyapi, name='pyapi'),
    path("pyapihello",  views.pyapihello, name='pyapihello'),

]