from django.views.generic import ListView 
from .models import msgboard
class HomePageView(ListView):
    model = msgboard
    template_name = 'home.html'
    context_object_name='all_msgboard_list'
