from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    streak = models.IntegerField(default=0)
    last_marked_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name
    
