from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    image = models.FileField(upload_to='user_posts_file', default="")
    description =  models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='user')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return f"{self.description}"

    @property
    def num_likes(self):
        return self.liked.all().count()
    


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

