# Generated by Django 4.2.3 on 2023-08-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavebalance',
            name='days_left',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
