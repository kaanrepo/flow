# Generated by Django 4.2.6 on 2023-10-27 19:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_alter_request_reviewed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
