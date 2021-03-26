# Generated by Django 2.2 on 2020-08-31 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_salarypackage_total_salary_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='salary_package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employee.SalaryPackage'),
            preserve_default=False,
        ),
    ]