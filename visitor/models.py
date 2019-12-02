from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
# Create your models here.


class VisitorModel(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    title = models.CharField(max_length=254)
    created_by = models.ForeignKey(User, related_name='user_visitor', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "home"
        )