from django.db import models

# Create your models here.


class Posts(models.Model):
    image = models.ImageField(upload_to='images', default="")
    description =  models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.description}"
