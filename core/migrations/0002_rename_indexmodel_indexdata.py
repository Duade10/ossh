# Generated by Django 4.2.3 on 2023-07-15 07:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="IndexModel",
            new_name="IndexData",
        ),
    ]