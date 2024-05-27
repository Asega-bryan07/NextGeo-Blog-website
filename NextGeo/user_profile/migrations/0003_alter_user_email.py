# Generated by Django 4.2.13 on 2024-05-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "002_auto_20240518_1632"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "Email must be unique"},
                max_length=150,
                unique=True,
            ),
        ),
    ]