# Generated by Django 4.2.5 on 2023-09-08 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_books_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]