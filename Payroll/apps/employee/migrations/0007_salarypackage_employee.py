# Generated by Django 2.2 on 2020-08-30 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20200830_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarypackage',
            name='employee',
            field=models.ForeignKey(db_column='official_email', default=0, on_delete=django.db.models.deletion.PROTECT, to='employee.Employee'),
            preserve_default=False,
        ),
    ]
