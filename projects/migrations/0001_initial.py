# Generated by Django 4.2.3 on 2023-07-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("image", models.ImageField(upload_to="projects/")),
                ("title", models.CharField(max_length=3500)),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
