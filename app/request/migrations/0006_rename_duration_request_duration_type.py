# Generated by Django 4.2.6 on 2023-11-06 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_remove_request_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='duration',
            new_name='duration_type',
        ),
    ]