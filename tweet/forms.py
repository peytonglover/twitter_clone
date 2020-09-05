from django import forms
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class AddTweet(forms.Form):
    content=forms.CharField(max_length=140)

    class Meta:
        model = TwitterUser
        fields = ['tagname', 'bio']