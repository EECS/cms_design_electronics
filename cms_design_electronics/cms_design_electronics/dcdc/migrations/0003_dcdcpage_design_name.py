# Generated by Django 2.1.8 on 2019-04-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcdc', '0002_auto_20190401_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcdcpage',
            name='design_name',
            field=models.CharField(max_length=75, null=True, verbose_name='DC/DC Converter Name'),
        ),
    ]