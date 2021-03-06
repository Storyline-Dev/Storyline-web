# Generated by Django 4.0.5 on 2022-07-09 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storylineapp', '0002_address_bodyscan_clinician_counselingnotes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('race', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('startDate', models.DateField(verbose_name='Start Date')),
                ('lastSession', models.DateField(verbose_name='Last Session Date')),
                ('numOfSessions', models.IntegerField()),
                ('activityStatus', models.BooleanField()),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
