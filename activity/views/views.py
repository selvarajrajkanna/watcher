from activity.models import Users, ActivityPeriod
from activity.forms import UserActivityForms

from django.http import JsonResponse
from django.core import serializers
import datetime


def createuseractivity(request):
    if request.method == 'GET':
        total_days = 3
        for day in range(1, total_days + 1):
            base_datetime = datetime.datetime.now() - datetime.timedelta(days=total_days - day)
            for user in Users.objects.all():
                minutes_to_add = 20
                minutes_to_subtract = 15
                if user.id % 2 == 0:
                    minutes_to_add = 120
                    minutes_to_subtract = 115

                start_time = base_datetime - datetime.timedelta(minutes=minutes_to_subtract)
                end_time = base_datetime + datetime.timedelta(minutes=minutes_to_add)
                data = {
                    "start_time": start_time,
                    "end_time": end_time,
                    "user": user
                }
                activity = UserActivityForms(data=data)
                if activity.is_valid():
                    activity.save()
        return JsonResponse({"ok": True}, status=200)
    else:
        return JsonResponse(data={}, status=403)


def getuseractivity(request):
    if request.method == 'GET':
        data = {
            "ok": True,
            "members": []
        }
        for user in Users.objects.all():
            member = {
                "id": user.user_id,
                "real_name": user.name,
                "tz": user.timezone,
                "activity_periods": []
            }
            for activity in ActivityPeriod.objects.filter(user=user):
                time_format = '%b %#d %Y  %I:%M%p'
                member["activity_periods"].append(
                    {
                        "start_time": activity.start_time.strftime(time_format),
                        "end_time": activity.end_time.strftime(time_format)
                    }
                )
            data['members'].append(member)
        return JsonResponse(data= data, status=200)
    else:
        return JsonResponse(data={}, status=403)
