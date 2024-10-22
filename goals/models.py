from django.db import models
from django.conf import settings

class Goal(models.Model):
    GOAL_TYPES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance', 'Endurance'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPES)
    target_value = models.DecimalField(max_digits=6, decimal_places=2)
    current_value = models.DecimalField(max_digits=6, decimal_places=2)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "goals"
