from datetime import timedelta
from urllib import response
from django.utils import timezone
from .models import ProfileModel

class OnlineStatusmiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_profile = ProfileModel.objects.get(user=request.user)
            user_profile.last_activity = timezone.now()
            user_profile.is_online =True
            user_profile.save()


        response = self.get_response(request)


        online_threshold = timezone.now() - timedelta(minutes=15)
        online_users = ProfileModel.objects.filter(last_activity__gte=online_threshold)
        for user_profile in online_users:
            user_profile.is_online = True
            user_profile.save()

        return response