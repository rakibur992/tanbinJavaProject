# Generated by Django 2.2 on 2021-03-30 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0037_remove_employee_advance_tax_paid_last_financial_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeetaxadvencepayment',
            options={'verbose_name': 'Employee Tax Advence Payment', 'verbose_name_plural': 'Employee Tax Advence Payments'},
        ),
    ]
