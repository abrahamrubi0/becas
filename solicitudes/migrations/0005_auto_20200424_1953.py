# Generated by Django 2.2.6 on 2020-04-25 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_auto_20200424_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
