# Generated by Django 2.2 on 2020-09-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20200901_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialyear',
            name='financial_year_start',
            field=models.DateField(),
        ),
    ]