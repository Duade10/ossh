# Generated by Django 4.2.3 on 2023-07-21 08:43

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="event/main/")),
                ("title", models.CharField(max_length=4500)),
                (
                    "description",
                    froala_editor.fields.FroalaField(blank=True, null=True),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("full_name", models.CharField(max_length=500)),
                ("email_address", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=15)),
                (
                    "organization",
                    models.CharField(blank=True, max_length=1500, null=True),
                ),
                (
                    "participant_type",
                    models.CharField(
                        blank=True,
                        choices=[("Teams", "teams"), ("Individial", "Individual")],
                        max_length=15,
                        null=True,
                    ),
                ),
                ("number_of_participants", models.IntegerField(blank=True, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="events.event",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("file", models.ImageField(upload_to="events/sub/")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
