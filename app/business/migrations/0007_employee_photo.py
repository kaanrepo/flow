# Generated by Django 4.2.6 on 2023-10-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_customer_contact_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
