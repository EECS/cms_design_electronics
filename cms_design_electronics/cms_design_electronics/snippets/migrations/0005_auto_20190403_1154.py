# Generated by Django 2.1.8 on 2019-04-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20190403_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcdcdesignequations',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcdcdesignparam',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcdcreccomps',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dcdcselcomps',
            name='units',
            field=models.CharField(choices=[('kHz', 'kHz'), ('microHenries', 'microHenries'), ('microFarads', 'microFarads'), ('Volts', 'V'), ('Amps', 'A'), ('', None), ('%', '%'), ('Ohms', 'Ohms')], max_length=50, null=True),
        ),
    ]