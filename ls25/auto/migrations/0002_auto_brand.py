# Generated by Django 5.0.1 on 2024-01-30 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auto.brandauto'),
            preserve_default=False,
        ),
    ]
