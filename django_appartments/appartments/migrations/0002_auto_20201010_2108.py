# Generated by Django 3.0.8 on 2020-10-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartment',
            name='price',
            field=models.FloatField(),
        ),
    ]
