# Generated by Django 4.2.6 on 2023-10-21 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_alter_employee_alocation_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.employee'),
        ),
    ]
