from .models import VisitorModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import JsonResponse
from visitor.forms import VisitorForm


# Create your views here.
class VisitorHome(generic.TemplateView):
    template_name = 'visitor/visitor_index.html'


class VisitorList(generic.View):
    def get(self, request):
        visitors = list(VisitorModel.objects.all().values())
        data = {'visitors': visitors}
        return JsonResponse(data)


class CreateVisitor(LoginRequiredMixin, generic.View):
    form_class = VisitorForm
    initial = {'key': 'value'}

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_model = VisitorModel.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                title=form.cleaned_data['title'],
                created_by=self.request.user
            )
            data = {
                'is_valid': True,
                'form': new_model.pk
            }
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class VisitorUpdateView(LoginRequiredMixin, generic.View):
    form_class = VisitorForm

    def post(self, request, pk):
        visitor = VisitorModel.objects.get(pk=pk)
        form = self.form_class(request.POST)
        data = dict()
        if form.is_valid():
            visitor.title = form.cleaned_data['title']
            visitor.email = form.cleaned_data['email']
            visitor.name = form.cleaned_data['name']
            visitor.save()
            data['is_valid'] = True
            data['form'] = visitor.pk
        else:
            data['is_valid'] = False
        return JsonResponse(data)


class VisitorDeleteView(LoginRequiredMixin, generic.View):

    def post(self, request, pk):
        data = dict()
        visitor = VisitorModel.objects.get(pk=pk)
        if visitor:
            visitor.delete()
            data['message'] = "visitor deleted!"
        else:
            data['message'] = "Error!"
        return JsonResponse(data)
