# Generated by Django 5.0.7 on 2024-09-04 06:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_customuser_delete_users"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="first_name",
            new_name="firstname",
        ),
        migrations.RenameField(
            model_name="customuser",
            old_name="last_name",
            new_name="lastname",
        ),
    ]
