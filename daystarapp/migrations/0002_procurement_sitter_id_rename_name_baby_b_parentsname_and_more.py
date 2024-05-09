# Generated by Django 5.0.4 on 2024-05-07 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('procurement_date', models.DateField(auto_now_add=True)),
                ('procurement_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='baby',
            old_name='name',
            new_name='b_parentsname',
        ),
        migrations.RemoveField(
            model_name='baby',
            name='parent',
        ),
        migrations.AddField(
            model_name='baby',
            name='baby_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daystarapp.baby_id'),
        ),
        migrations.AlterField(
            model_name='baby',
            name='timein',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='baby',
            name='timeout',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_mode', models.CharField(blank=True, choices=[('daily', 'Daily'), ('monthly', 'Monthly')], max_length=100, null=True)),
                ('payment_type', models.CharField(choices=[('halfday', 'Half Day'), ('fullday', 'Full Day')], max_length=10)),
                ('payment_currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('UGX', 'UGX')], max_length=10, null=True)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('payment_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daystarapp.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_firstname', models.CharField(max_length=100)),
                ('s_lastname', models.CharField(max_length=100)),
                ('s_gender', models.CharField(max_length=100)),
                ('s_age', models.PositiveIntegerField()),
                ('s_location', models.CharField(default='Kabalagala', max_length=100)),
                ('s_nextofkin', models.CharField(max_length=100)),
                ('s_NIN', models.CharField(max_length=100)),
                ('s_recommendersname', models.CharField(max_length=100)),
                ('s_educationlevel', models.CharField(max_length=100)),
                ('s_contact', models.CharField(max_length=100)),
                ('sitter_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daystarapp.sitter_id')),
            ],
        ),
    ]
