# Generated by Django 2.2 on 2020-12-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0029_auto_20201002_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gross_monthly_salary',
            field=models.FloatField(default=0.0),
        ),
    ]