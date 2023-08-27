# Generated by Django 4.2.4 on 2023-08-21 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('method', models.CharField(choices=[('TELEBIRR', 'TELEBIRR'), ('CBE', 'CBE'), ('CHAPA', 'CHAPA')], max_length=200)),
                ('tnx_id', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('PAID', 'PAID'), ('NOT PAID', 'NOT PAID'), ('PENDING', 'PENDING')], default='NOT PAID', max_length=200)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
            ],
        ),
    ]
