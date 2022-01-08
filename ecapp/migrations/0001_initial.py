# Generated by Django 3.2.11 on 2022-01-07 15:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('temperature', models.FloatField(default=10.1)),
            ],
            options={
                'verbose_name_plural': 'cities',
                'ordering': ('name',),
            },
        ),
    ]
