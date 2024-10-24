# Generated by Django 4.1.13 on 2024-10-22 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')], max_length=50)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=6)),
                ('proteins', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fats', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=6)),
                ('meal_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'meals',
            },
        ),
    ]
