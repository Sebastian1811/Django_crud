# Generated by Django 4.0.4 on 2022-04-22 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='categoria',
            field=models.CharField(default='comida', max_length=30),
        ),
        migrations.AddField(
            model_name='plato',
            name='tiempo_preparaciona',
            field=models.IntegerField(default=30),
        ),
    ]