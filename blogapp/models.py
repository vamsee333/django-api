from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
# Create your models here.
class Blogpost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True,blank=True)
    content=models.TextField(max_length=1000,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user

    def get_api_url(self):
        return api_reverse("blog-post",kwargs={'pk':self.pk})

