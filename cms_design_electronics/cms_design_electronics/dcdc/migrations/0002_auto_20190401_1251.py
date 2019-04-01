# Generated by Django 2.1.8 on 2019-04-01 19:51

import cms_design_electronics.streams.blocks
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
        ('dcdc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcdcpage',
            name='design_equations',
            field=modelcluster.fields.ParentalManyToManyField(related_name='_dcdcpage_design_equations_+', to='snippets.DCDCDesignEquations', verbose_name='Design Equations'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='dcdc_type',
            field=models.CharField(choices=[('ccm', 'Continuous Conduction Mode'), ('dcm', 'Discontinuous Conduction Mode')], max_length=75, null=True, verbose_name='DC/DC Current Type'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='design_description',
            field=wagtail.core.fields.StreamField([('description', cms_design_electronics.streams.blocks.RichtextBlock())], null=True, verbose_name='Design Description'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='design_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Circuit Image'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='design_params',
            field=modelcluster.fields.ParentalManyToManyField(related_name='_dcdcpage_design_params_+', to='snippets.DCDCDesignParam', verbose_name='Design Parameters'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='open_loop_equations',
            field=modelcluster.fields.ParentalManyToManyField(related_name='_dcdcpage_open_loop_equations_+', to='snippets.DCDCOpenLoopEquations', verbose_name='Open Loop Transfer Functions'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='recommended_components',
            field=modelcluster.fields.ParentalManyToManyField(related_name='_dcdcpage_recommended_components_+', to='snippets.DCDCRecComps', verbose_name='Recommended Components'),
        ),
        migrations.AlterField(
            model_name='dcdcpage',
            name='selected_components',
            field=modelcluster.fields.ParentalManyToManyField(related_name='_dcdcpage_selected_components_+', to='snippets.DCDCSelComps', verbose_name='Selected Components'),
        ),
    ]
