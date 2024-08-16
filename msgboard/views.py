from django.views.generic import ListView, CreateView
from .models import msgboard
from django.http import HttpResponse
# class HomePageView(ListView):
#     model = msgboard
#     template_name = 'home.html'
#     context_object_name='all_msgboard_list'


def home(request):
    return HttpResponse("Hey I'm up and running hurray checkout my another project on crud <a href='https://djangodeploy-6i7w.onrender.com/crud'>CRUD APP</a>")