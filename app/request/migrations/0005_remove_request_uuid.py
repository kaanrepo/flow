# Generated by Django 4.2.6 on 2023-11-06 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_request_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='uuid',
        ),
    ]
