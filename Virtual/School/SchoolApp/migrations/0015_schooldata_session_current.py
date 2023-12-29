# Generated by Django 4.2.5 on 2023-12-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0014_alter_result_grade_alter_result_totalscore'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]