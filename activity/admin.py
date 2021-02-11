from django.contrib import admin
from activity.models import (
    Users,
    ActivityPeriod
)

admin.site.register(Users)
admin.site.register(ActivityPeriod)
