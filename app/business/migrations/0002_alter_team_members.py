# Generated by Django 4.2.6 on 2023-10-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='related_team', to='business.employee'),
        ),
    ]