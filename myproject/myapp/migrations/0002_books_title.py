# Generated by Django 4.2.5 on 2023-09-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='title',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
