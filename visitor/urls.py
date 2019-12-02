from django.urls import path
from .views import VisitorList,CreateVisitor,VisitorUpdateView,VisitorDeleteView

app_name = 'visitors'

urlpatterns = [
    path('', VisitorList.as_view(), name='list'),
    path('new/', CreateVisitor.as_view(), name='create'),
    path('update/<int:pk>', VisitorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', VisitorDeleteView.as_view(), name='delete'),
]