# Generated by Django 4.2.7 on 2023-11-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_physio_form_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physio_form',
            name='time',
            field=models.CharField(max_length=15),
        ),
    ]