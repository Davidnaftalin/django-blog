from django.views.generic import ListView, DetailView, FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView

from .models import Blog
from .forms import SubmitForm


class HomeView(ListView):
    template_name = 'bloglist.html'
    model = Blog

class PermaView(DetailView):
    template_name = 'detail.html'
    model = Blog


class SignUpFormView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name  = 'register.html'
    success_url = '/'

class SubmitFormView(CreateView):
    form_class = SubmitForm
    template_name = 'submit.html'
    success_url = '/'

    def form_valid(self, form):
        blog_post = form.save(commit=False)
        blog_post.author = self.request.user  # use your own profile here
        blog_post.save()
        return HttpResponseRedirect('/')
