# Generated by Django 4.2.5 on 2023-12-14 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0016_schoolimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolimage',
            name='Data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='SchoolApp.schooldata'),
        ),
    ]