# Generated by Django 5.1.3 on 2024-12-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aonewebs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aoneeducational',
            name='first_choices',
            field=models.CharField(max_length=250, verbose_name='first Institution'),
        ),
        migrations.AlterField(
            model_name='aoneeducational',
            name='second_choices',
            field=models.CharField(max_length=250, verbose_name='second Institution'),
        ),
    ]
