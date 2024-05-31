from django.contrib.auth.models import User
from django.db import models






class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='friendship_from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friendship_to_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.username} - {self.to_user.username}"
