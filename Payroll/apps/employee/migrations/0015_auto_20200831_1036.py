# Generated by Django 2.2 on 2020-08-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_auto_20200831_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='tax_1',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='payroll',
            name='tax_2',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='payroll',
            name='tax_3',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='payroll',
            name='tax_4',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='payroll',
            name='tax_5',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]