# Generated by Django 3.2.11 on 2022-01-08 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0003_alter_weathertask_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weathertask',
            name='temperature',
        ),
    ]
