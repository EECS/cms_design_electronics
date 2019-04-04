# Generated by Django 2.1.8 on 2019-04-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20190403_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcdcdesignequations',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('Duty Cycle', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcdcdesignparam',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('Duty Cycle', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcdcreccomps',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('Duty Cycle', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcdcselcomps',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('Duty Cycle', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
    ]