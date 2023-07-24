# Generated by Django 4.2.3 on 2023-07-16 11:42

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_aboutdata_options_alter_indexdata_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoundryDataContent",
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
                ("content", froala_editor.fields.FroalaField()),
            ],
            options={
                "verbose_name": "Foundry Page Content",
                "verbose_name_plural": "Foundry Page Content",
            },
        ),
    ]
