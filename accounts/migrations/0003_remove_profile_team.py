# Generated by Django 2.0.1 on 2018-01-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180128_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='team',
        ),
    ]
