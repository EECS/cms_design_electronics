# Generated by Django 2.0.9 on 2019-03-25 17:03

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190325_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(blank=True, help_text='Site title link, to be differentiated from other links in header.', max_length=255, null=True)),
                ('header_links', wagtail.core.fields.StreamField([('link1', wagtail.core.blocks.CharBlock(classname='full title')), ('link2', wagtail.core.blocks.CharBlock(classname='full title')), ('link3', wagtail.core.blocks.CharBlock(classname='full title')), ('link4', wagtail.core.blocks.CharBlock(classname='full title'))])),
            ],
            options={
                'verbose_name_plural': 'Header Text',
            },
        ),
    ]
