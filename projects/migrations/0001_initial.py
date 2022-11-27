# Generated by Django 4.1.3 on 2022-11-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('topic', models.CharField(choices=[('DE', 'Data Engineering'), ('ML', 'Machine Learning'), ('BI', 'Business Intelligence'), ('WD', 'Web Development'), ('SE', 'Software Engineering'), ('O', 'Other')], max_length=2)),
                ('tech_stack', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]