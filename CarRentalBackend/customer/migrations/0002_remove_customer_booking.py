# Generated by Django 4.2.4 on 2023-09-04 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='booking',
        ),
    ]
