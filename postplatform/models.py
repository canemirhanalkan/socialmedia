from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    image = models.ImageField(upload_to='images', default="")
    description =  models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"
