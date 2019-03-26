# Generated by Django 2.0.9 on 2019-03-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190325_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='header',
            options={'verbose_name': 'Header Text'},
        ),
        migrations.AddField(
            model_name='header',
            name='header_name',
            field=models.TextField(default='Default.', help_text='Fill in the page for which this header exists.'),
        ),
        migrations.AddField(
            model_name='header',
            name='path_info',
            field=models.CharField(default='/', help_text='Fill in the relative path info for current header.', max_length=100),
        ),
    ]