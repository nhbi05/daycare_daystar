# Generated by Django 5.0.4 on 2024-04-30 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarapp', '0002_rename_parent_baby_babyno_remove_baby_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='babyno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daystarapp.baby_id'),
        ),
    ]
