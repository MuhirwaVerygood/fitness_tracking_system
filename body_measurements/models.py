from django.db import models
from django.conf import settings

class BodyMeasurement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist_circumference = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_taken = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "body_measurements"
