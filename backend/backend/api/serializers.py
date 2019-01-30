from django.contrib.auth.models import User
from .models import ActivityCenter
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

        class Meta:
                model = User
                fields = ('id', 'email')

class ActivityCenterSerializer(serializers.ModelSerializer):

        class Meta:
                model = ActivityCenter
                fields = ('id', 'activity', 'coordinator', 'duration', 'event date', 'event time')
