# Generated by Django 4.2.6 on 2023-11-02 14:12

import SchoolApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0005_alter_studentresult_remarkfromprincipal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='session',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.session', unique=SchoolApp.models.Student),
        ),
    ]