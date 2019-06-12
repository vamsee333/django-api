from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class poll(models.Model):
    question= models.CharField(max_length=1000)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll=models.ForeignKey(poll,related_name='choices',on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=1000)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice=models.ForeignKey(Choice,related_name='votes',on_delete=models.CASCADE)
    poll=models.ForeignKey(poll,on_delete=models.CASCADE)
    voted_by=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together=('poll','voted_by')





