# Generated by Django 2.2 on 2021-01-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20210116_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
