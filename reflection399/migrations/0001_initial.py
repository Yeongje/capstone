# Generated by Django 2.0.1 on 2018-04-20 13:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reflection399',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('team_number', models.IntegerField(blank=True, null=True)),
                ('week', models.IntegerField(blank=True, null=True)),
                ('grade', models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('self_reflection', models.TextField(help_text='Reflect on how you delivered on your three main tasks for the last fortnight', verbose_name='self_reflection')),
                ('self_plan', models.TextField(help_text='Detail your three main tasks for the next fortnight', verbose_name='self_plan')),
                ('team1_name', models.CharField(help_text='Write your team member name', max_length=100, verbose_name='team1_name')),
                ('team1_grade', models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('team1_reflection', models.TextField(help_text='Evaluation of contribution and performance ', verbose_name='team1_reflection')),
                ('team2_name', models.CharField(help_text='Write your team member name', max_length=100, verbose_name='team2_name')),
                ('team2_grade', models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('team2_reflection', models.TextField(help_text='Evaluation of contribution and performance ', verbose_name='team2_reflection')),
                ('team3_name', models.CharField(help_text='Write your team member name', max_length=100, verbose_name='team3_name')),
                ('team3_grade', models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('team3_reflection', models.TextField(help_text='Evaluation of contribution and performance ', verbose_name='team3_reflection')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1)),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['team_number'],
            },
        ),
    ]
