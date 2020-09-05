from django.shortcuts import render
from notification.models import Notification

# Create your views here.

def notification_view(request):
    notifications = Notification.objects.all()
    unread = []
    for notification in notifications:
        if notification.read_status == False:
            unread.append(notification)
            notification.read_status = True
            notification.save()
    return render(request, 'notifications.html', {'unread': unread})