from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.forms import AddTweet
from tweet.models import Tweet
from notification.models import Notification
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
import re
# Create your views here.

def create_tweet(request):
    if request.method == 'POST':
        form =AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                content=data.get('content'),
                posted_by= request.user,
                posted_at= datetime.now()
            )
            mentions = re.findall(r'@(\w+)', data.get('content'))
            if mentions:
                users = TwitterUser.objects.all()
                for mention in mentions:
                    if TwitterUser.objects.get(username=mention):
                        Notification.objects.create(
                            tweet_notification = new_tweet,
                            notified_user = TwitterUser.objects.get(username=mention)
                        )
            if new_tweet:
                poster = request.user
                poster.tweetcount += 1
                poster.save()
                return HttpResponseRedirect(reverse('homepage'))
    form = AddTweet()
    return render(request, 'tweetform.html', {'form': form})

def tweet_detail(request, tweet_id):
    selected_tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, 'tweetdetail.html', {'selected_tweet': selected_tweet})



