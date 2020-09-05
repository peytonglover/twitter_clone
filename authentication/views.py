from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from authentication.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    all_tweets = Tweet.objects.all().order_by('-posted_at')
    following = request.user.following.all()
    return render(request, 'index.html', {'all_tweets': all_tweets, 'following': following})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_twitter_user = TwitterUser.objects.create_user(username=data.get('username'),  password=data.get('password'), tagname=data.get('tagname'), bio=data.get('bio'))
            login(request, new_twitter_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignUpForm()
    return render(request, 'signupform.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, 'loginform.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))