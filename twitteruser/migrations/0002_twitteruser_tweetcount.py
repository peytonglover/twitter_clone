# Generated by Django 3.1.1 on 2020-09-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='tweetcount',
            field=models.IntegerField(default=0),
        ),
    ]
