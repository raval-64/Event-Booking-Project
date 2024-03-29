# Generated by Django 2.2.6 on 2019-10-16 07:32

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('trek', 'Trek'), ('comedy', 'Comedy'), ('music', 'Music'), ('adventure', 'Adventure'), ('art', 'Art'), ('dance', 'Dance'), ('game', 'Games'), ('food', 'Food Fest'), ('other', 'Other')], max_length=10)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField()),
                ('price', models.FloatField(max_length=10)),
                ('seats', models.IntegerField(max_length=3)),
                ('booked_seats', models.IntegerField(max_length=3)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            options={
                'verbose_name': 'booking',
                'verbose_name_plural': 'bookings',
            },
        ),
    ]
