from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser
# Create your models here.

class Notification(models.Model):
    tweet_notification = models.ForeignKey(Tweet, on_delete=models.CASCADE, default=None)
    notified_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, default=None)
    read_status = models.BooleanField(default=False)

