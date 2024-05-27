# Generated by Django 4.2.13 on 2024-05-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notification", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="notification_types",
            field=models.CharField(
                choices=[("Blog", "Blog"), ("Like", "Like"), ("Follow", "Follow")],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="text",
            field=models.CharField(max_length=250),
        ),
    ]