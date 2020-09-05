from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def user_page(request, user_name):
    all_tweets= Tweet.objects.all().order_by('-posted_at')
    selected_user = TwitterUser.objects.filter(username=user_name).first()
    following = request.user.following.all()
    followcount = (selected_user.following.all().count() - 1)
    return render(request, 'userdetail.html', {'selected_user': selected_user, 'all_tweets': all_tweets, 'following': following, 'followcount': followcount})


def follow_view(request, user_id):
    user = request.user
    selected_user = TwitterUser.objects.get(id=user_id)
    user.following.add(selected_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unfollow_view(request, user_id):
    user = request.user
    selected_user = TwitterUser.objects.get(id=user_id)
    user.following.remove(selected_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
