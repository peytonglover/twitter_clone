from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    tagname = models.CharField(max_length=80, unique=True)
    bio = models.CharField(max_length=140)
    tweetcount = models.IntegerField(default=0)
    following = models.ManyToManyField('self', symmetrical=False)


