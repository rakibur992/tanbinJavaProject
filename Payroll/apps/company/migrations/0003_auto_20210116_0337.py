# Generated by Django 2.2 on 2021-01-15 21:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210116_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]