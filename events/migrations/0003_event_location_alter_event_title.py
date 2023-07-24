# Generated by Django 4.2.3 on 2023-07-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_event_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="title",
            field=models.CharField(max_length=2500),
        ),
    ]
