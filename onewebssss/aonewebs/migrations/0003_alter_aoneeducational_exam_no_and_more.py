# Generated by Django 5.1.3 on 2024-12-13 23:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aonewebs', '0002_alter_aoneeducational_first_choices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aoneeducational',
            name='exam_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Exam Number'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='mobile_number',
            field=models.BigIntegerField(verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='nin',
            field=models.BigIntegerField(verbose_name='NIN'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='num_of_sit',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)], verbose_name='Number of Sittings'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='phone_no',
            field=models.BigIntegerField(verbose_name='Parent Phone Number'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='pin_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Pin'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='profile_code',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Profile Code'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='serial_no',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Serial Number'),
        ),
    ]
