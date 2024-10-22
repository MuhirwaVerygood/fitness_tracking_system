from django.db import models
from django.conf import settings

class DailyActivity(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    steps = models.PositiveIntegerField()
    active_minutes = models.PositiveIntegerField()
    calories_burned = models.DecimalField(max_digits=6, decimal_places=2)
    activity_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "daily_activities"
