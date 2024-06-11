from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#------------post model----------#
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
    


#------------like model----------#
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



# #------------comment model----------#

class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} {self.post.id}"
    
