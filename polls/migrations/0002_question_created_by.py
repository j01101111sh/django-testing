# Generated by Django 4.2.7 on 2023-11-28 04:30
# pylint: disable=invalid-name
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="created_by",
            field=models.CharField(default="Josh", max_length=50),
        ),
    ]