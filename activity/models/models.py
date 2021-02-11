from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Users(BaseModel):
    name = models.TextField(null=False)
    user_id = models.TextField(null=False)
    timezone = models.TextField(null=False)


class ActivityPeriod(BaseModel):
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    user = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)
