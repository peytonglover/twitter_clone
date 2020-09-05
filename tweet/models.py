from django.db import models
from twitteruser.models import TwitterUser

# Create your models here.
class Tweet(models.Model):
    content = models.CharField(max_length=140)
    posted_by = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    posted_at = models.DateTimeField()
    
    