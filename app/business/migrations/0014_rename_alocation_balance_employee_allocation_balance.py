# Generated by Django 4.2.6 on 2023-11-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0013_customer_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='alocation_balance',
            new_name='allocation_balance',
        ),
    ]