from django.urls import path
from visitor import views

app_name = 'visitors'

urlpatterns = [
    path('', views.VisitorHome.as_view(), name='home'),
    path('all/', views.VisitorList.as_view(), name='list'),
    path('new/', views.CreateVisitor.as_view(), name='create'),
    path('update/<int:pk>', views.VisitorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.VisitorDeleteView.as_view(), name='delete'),
]