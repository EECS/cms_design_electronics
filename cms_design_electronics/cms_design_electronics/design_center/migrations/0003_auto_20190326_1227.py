# Generated by Django 2.0.9 on 2019-03-26 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design_center', '0002_auto_20190326_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designcenter',
            options={'verbose_name': 'Design Center Design', 'verbose_name_plural': 'Design Center Designs'},
        ),
        migrations.RenameField(
            model_name='designcenter',
            old_name='test',
            new_name='design_name',
        ),
    ]