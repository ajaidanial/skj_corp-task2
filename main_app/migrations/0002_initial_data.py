"""This file loads the initial data into the database on `migrate`."""
from django.contrib.auth.models import User
from django.db import migrations

from task2.settings import ADMIN_USER


def create_super_user(apps, schema_editor):
    # create the app super user
    User.objects.create_superuser(
        email=ADMIN_USER["username"],
        username=ADMIN_USER["username"],
        password=ADMIN_USER["password"],
        first_name="Admin",
        last_name="User",
    )


def delete_super_user(apps, schema_editor):
    # delete the app super user
    User.objects.get(email=ADMIN_USER["username"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_super_user, reverse_code=delete_super_user),
    ]
