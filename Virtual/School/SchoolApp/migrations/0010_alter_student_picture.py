# Generated by Django 4.2.5 on 2023-11-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0009_alter_result_teacherincharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(upload_to='student-images'),
        ),
    ]