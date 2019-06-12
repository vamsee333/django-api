from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blogpost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True,blank=True)
    content=models.TextField(max_length=1000,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)



