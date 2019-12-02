from .models import VisitorModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.views.generic import CreateView,DeleteView,ListView,UpdateView


# Create your views here.

class VisitorList(ListView):
    model = VisitorModel



class CreateVisitor(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ("name","email","title")
    model = VisitorModel

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

class VisitorUpdateView(LoginRequiredMixin,UpdateView):
    fields = ("name", "email", "title")
    model = VisitorModel

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

class VisitorDeleteView(DeleteView):
    model = VisitorModel
    success_url = reverse_lazy('visitors:list')