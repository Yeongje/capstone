# Generated by Django 2.0.1 on 2018-04-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_post_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('w', 'Web Application'), ('m', 'Mobile Application'), ('s', 'Software'), ('h', 'Hardware'), ('d', 'Data')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
