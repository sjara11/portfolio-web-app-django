# Generated by Django 4.1.3 on 2022-12-05 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="author",
            field=models.CharField(default="TestUser", max_length=60),
        ),
    ]
