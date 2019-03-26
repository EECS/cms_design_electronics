# Generated by Django 2.0.9 on 2019-03-26 19:07

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCDC',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.TextField(blank=True, help_text='Name of the DC/DC converter.')),
                ('description', models.TextField(blank=True, help_text='Text to describe the DC/DC converter.')),
            ],
            options={
                'verbose_name': 'DC/DC Converters',
                'verbose_name_plural': 'DC/DC Converters',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DCDCType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'DC/DC Converter Types (CCM vs. DCM)',
                'verbose_name_plural': 'DC/DC Converter Types (CCM vs. DCM)',
            },
        ),
        migrations.CreateModel(
            name='DesignEquations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(help_text='Duty Ratio etc.', max_length=100)),
                ('converter', models.CharField(max_length=100)),
                ('equation', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'DC/DC Converter Design Equations for Analysis',
            },
        ),
        migrations.CreateModel(
            name='DesignParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=100)),
                ('descr', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'DC/DC Converter Design Parameters',
            },
        ),
        migrations.CreateModel(
            name='OpenLoopEquations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(help_text='Input to Output Transfer etc.', max_length=100)),
                ('equation', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'DC/DC Converter Open Loop Design Equations',
            },
        ),
        migrations.CreateModel(
            name='RecComps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=100)),
                ('descr', models.CharField(help_text='C1 vs. L1 vs. etc.', max_length=100)),
                ('converter', models.CharField(max_length=100)),
                ('equation', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'DC/DC Converter Recommended Components',
            },
        ),
        migrations.CreateModel(
            name='SelComps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=100)),
                ('descr', models.CharField(help_text='C1 vs. L1 vs. etc.', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'DC/DC Converter Selected Components for Analysis',
            },
        ),
        migrations.AddField(
            model_name='dcdc',
            name='converter_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcdc_converters.DCDCType'),
        ),
        migrations.AddField(
            model_name='dcdc',
            name='design_equations',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='dcdc_converters.DesignEquations'),
        ),
        migrations.AddField(
            model_name='dcdc',
            name='design_parameters',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='dcdc_converters.DesignParam'),
        ),
        migrations.AddField(
            model_name='dcdc',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='dcdc',
            name='open_loop_equations',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='dcdc_converters.OpenLoopEquations'),
        ),
        migrations.AddField(
            model_name='dcdc',
            name='recommended_components',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='dcdc_converters.RecComps'),
        ),
        migrations.AddField(
            model_name='dcdc',
            name='selected_components',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='dcdc_converters.SelComps'),
        ),
    ]