# Generated by Django 4.2.6 on 2023-10-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_alter_team_coordinator_alter_team_leader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='alocation_balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='yearly_allocation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]