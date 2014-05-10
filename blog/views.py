from django.views.generic import ListView
from .models import Blog


class HomeView(ListView):
    template_name = 'bloglist.html'
    model = Blog
