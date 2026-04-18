from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Habit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    streak = models.PositiveBigIntegerField(default=0)
    last_marked_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
    
