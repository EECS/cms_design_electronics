# Generated by Django 2.1.8 on 2019-04-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_dcdcdesignparam_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcdcdesignequations',
            name='units',
            field=models.CharField(choices=[('Switching Frequency', 'kHz'), ('Inductance', 'microHenries'), ('Capacitance', 'microFarads'), ('Volts', 'V'), ('Amps', 'A')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dcdcreccomps',
            name='units',
            field=models.CharField(choices=[('Switching Frequency', 'kHz'), ('Inductance', 'microHenries'), ('Capacitance', 'microFarads'), ('Volts', 'V'), ('Amps', 'A')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dcdcselcomps',
            name='units',
            field=models.CharField(choices=[('Switching Frequency', 'kHz'), ('Inductance', 'microHenries'), ('Capacitance', 'microFarads'), ('Volts', 'V'), ('Amps', 'A')], max_length=50, null=True),
        ),
    ]
