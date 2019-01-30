from django.contrib.auth.models import User
from django.db import models


# ==== Activity Center Model ==== #


class ActivityCenter(models.Model):
    activity = models.CharField(max_length=100)
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="creator")
    participant = models.ManyToManyField(User, related_name="joiner")
    duration = models.DurationField()
    date_of_event = models.DateField(auto_now_add=False)
    time_of_event = models.TimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s | %s | %s | %s" % (self.activity, self.coordinator, self.duration, self.number_of_participants)


    
