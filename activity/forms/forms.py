from django import forms
from activity.models import ActivityPeriod


class UserActivityForms(forms.ModelForm):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'
