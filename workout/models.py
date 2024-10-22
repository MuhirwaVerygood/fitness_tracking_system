from django.db import models
from django.conf import settings

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('gym', 'Gym'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPES)
    duration = models.PositiveIntegerField()  # in minutes
    calories_burned = models.DecimalField(max_digits=6, decimal_places=2)
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    workout_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "workouts"
