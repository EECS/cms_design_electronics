from django import forms
from django.db import models

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
    )

from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class DCDCType(models.Model):
    """
    A Django model to store the type of DC/DC Converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    model you'll see we use a ForeignKey to create the relationship between
    DCDCType and DCDCPage. This allows a single relationship (e.g only one
    DCDCType can be added) that is one-way (e.g. DCDCType will have no way to
    access related DCDCPage objects).
    """

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "DC/DC Converter Types (CCM vs. DCM)"
        verbose_name_plural = "DC/DC Converter Types (CCM vs. DCM)"

@register_snippet
class DesignParam(models.Model):
    """
    A Django model to store the design parameters in the DC/DC converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    abbreviation = models.CharField(max_length=100)
    descr = models.CharField(max_length=100)

    def __str__(self):
        return self.descr+", "+self.abbreviation

    class Meta:
        verbose_name_plural = "DC/DC Converter Design Parameters"

@register_snippet
class RecComps(models.Model):
    """
    A Django model to store the recommended components for the DC/DC converters.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    abbreviation = models.CharField(max_length=100)
    descr = models.CharField(max_length=100, help_text="C1 vs. L1 vs. etc.")
    converter = models.CharField(max_length=100)
    equation = models.TextField()

    def __str__(self):
        return self.descr+", " +self.abbreviation+", " +self.converter

    class Meta:
        verbose_name_plural = "DC/DC Converter Recommended Components"

@register_snippet
class SelComps(models.Model):
    """
    A Django model to store the selected components for the DC/DC converters.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    abbreviation = models.CharField(max_length=100)
    descr = models.CharField(max_length=100, help_text="C1 vs. L1 vs. etc.")

    def __str__(self):
        return self.descr

    class Meta:
        verbose_name_plural = "DC/DC Converter Selected Components for Analysis"

@register_snippet
class DesignEquations(models.Model):
    """
    A Django model to store the selected equations for design of the DC/DC converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    descr = models.CharField(max_length=100, help_text="Duty Ratio etc.")
    converter = models.CharField(max_length=100)
    equation = models.TextField()

    def __str__(self):
        return self.descr

    class Meta:
        verbose_name_plural = "DC/DC Converter Design Equations for Analysis"

@register_snippet
class OpenLoopEquations(models.Model):
    """
    A Django model to store the selected open loop design equations of the DC/DC converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    descr = models.CharField(max_length=100, help_text="Input to Output Transfer etc.")
    equation = models.TextField()

    def __str__(self):
        return self.descr

    class Meta:
        verbose_name_plural = "DC/DC Converter Open Loop Design Equations"

class DCDCPage(Page):
    """
    Detail view for a DC/DC converter.
    """
    name = models.TextField(
        help_text='Name of the DC/DC converter.',
        blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    description = models.TextField(
        help_text='Text to describe the DC/DC converter.',
        blank=True)

    converter_type = models.ForeignKey(
        DCDCType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    design_parameters = ParentalManyToManyField('DesignParam', blank=True)

    recommended_components = ParentalManyToManyField('RecComps', blank=True)

    selected_components = ParentalManyToManyField('SelComps', blank=True)

    design_equations = ParentalManyToManyField('DesignEquations', blank=True)

    open_loop_equations = ParentalManyToManyField('OpenLoopEquations', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('converter_type'),
        FieldPanel('design_parameters'),
        FieldPanel('recommended_components'),
        FieldPanel('selected_components'),
        FieldPanel('design_equations'),
        MultiFieldPanel(
            [
                FieldPanel(
                    'open_loop_equations'
                ),
            ],
            heading="Open Loop Analysis Equations",
            classname="collapsible"
        ),
    ]