# Generated by Django 4.2.5 on 2023-09-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0003_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
