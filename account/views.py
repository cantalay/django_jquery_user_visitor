from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import UserCreateForm

# Create your views here.

class Register(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'register.html'