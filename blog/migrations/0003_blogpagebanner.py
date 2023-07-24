# Generated by Django 4.2.3 on 2023-07-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPageBanner",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blog/banner/"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]