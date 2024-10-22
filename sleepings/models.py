from django.db import models
from django.conf import settings
class SleepLog(models.Model):
    SLEEP_QUALITY_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sleep_duration = models.PositiveIntegerField()  
    sleep_start = models.DateTimeField()
    sleep_end = models.DateTimeField()
    sleep_quality = models.CharField(max_length=20, choices=SLEEP_QUALITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sleep_logs"
