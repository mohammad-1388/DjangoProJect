# Generated by Django 3.2.2 on 2021-05-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='selected',
            field=models.BooleanField(verbose_name='فعال'),
        ),
    ]