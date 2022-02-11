from email.policy import default
from django.db import models
from django.utils import timezone
from authe.models import registermodel
# Create your models here.
class chatmodel(models.Model):
    cid=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    msg=models.CharField(max_length=500)
    datetime=models.DateTimeField(default=timezone.now)
    cimg=models.ImageField(upload_to='chatimg/', null=True)
    cfile=models.FileField(upload_to='chatdoc/',null=True)