from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
    )

from wagtail.snippets.models import register_snippet

from ..utils.utils import UNITS

@register_snippet
class DCDCDesignParam(models.Model):
    """
    A Django model to store the design parameters in the DC/DC converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    abbreviation = models.CharField(
                    max_length=100, 
                    blank=False, 
                    null=True,
                )

    description = models.CharField(
                max_length=100, 
                blank=False, 
                null=True,
            )
    
    units = models.CharField(
                max_length=50, 
                blank=False, 
                null=True,
                choices=UNITS,
            )

    def __str__(self):
        return self.description+", "+self.abbreviation

    class Meta:
        verbose_name = "DC/DC Converter: Design Parameter"
        verbose_name_plural = "DC/DC Converter: Design Parameters"

@register_snippet
class DCDCRecComps(models.Model):
    """
    A Django model to store the recommended components for the DC/DC converters.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    abbreviation = models.CharField(
                    max_length=100, 
                    blank=False, 
                    null=True,
                    help_text = "E.g. C1 vs. L1 vs. etc.",
                )

    converter = models.CharField(
                    max_length=150, 
                    blank=False, 
                    null=True,
                    help_text="E.g. CCM Buck Converter vs. etc."
                )

    equation = models.TextField(
                    blank=False, 
                    null=True,
                )
    
    units = models.CharField(
                max_length=50, 
                blank=False, 
                null=True,
                choices=UNITS,
            )

    def __str__(self):
        return self.abbreviation+", " +self.converter

    class Meta:
        verbose_name = "DC/DC Converter: Recommended Component"
        verbose_name_plural = "DC/DC Converter: Recommended Components"

@register_snippet
class DCDCSelComps(models.Model):
    """
    A Django model to store the selected components for the DC/DC converters.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    abbreviation = models.CharField(
                    max_length=100, 
                    blank=False, 
                    null=True,
                    help_text = "E.g. C1 vs. L1 vs. etc.",
                )

    units = models.CharField(
                max_length=50, 
                blank=False, 
                null=True,
                choices=UNITS,
            )

    def __str__(self):
        return self.abbreviation

    class Meta:
        verbose_name = "DC/DC Converter: Selected Component"
        verbose_name_plural = "DC/DC Converter: Selected Components"

@register_snippet
class DCDCDesignEquations(models.Model):
    """
    A Django model to store the selected equations for design of the DC/DC converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    description = models.CharField(
                    max_length=150, 
                    blank=False, 
                    null=True,
                    help_text="E.g. Duty Ratio etc."
                )

    converter = models.CharField(
                    max_length=100,
                    blank = False,
                    null=True,
                    help_text="E.g. CCM Buck Converter etc.",
                )

    equation = models.TextField(
                blank = False,
                null=True,
                help_text="Design Equation",
                )
    
    units = models.CharField(
                max_length=50, 
                blank=False, 
                null=True,
                choices=UNITS,
            )

    def __str__(self):
        return "{}, {}".format(self.description, self.converter)

    class Meta:
        verbose_name = "DC/DC Converter: Analysis Result"
        verbose_name_plural = "DC/DC Converter: Analysis Results"

@register_snippet
class DCDCOpenLoopEquations(models.Model):
    """
    A Django model to store the selected open loop design equations of the DC/DC converter.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the DCDCPage
    We use a new piece of functionality available to Wagtail called the 
    ParentalManyToManyField on the BreadPage model to display this.
    """

    description = models.CharField(
                    max_length=100,
                    blank = False,
                    null=True,
                    help_text="E.g. Input to Output Transfer etc."
                )

    converter = models.CharField(
                    max_length=100,
                    blank = False,
                    null=True,
                    help_text="E.g. CCM Buck Converter etc.",
                )

    equation = models.TextField(
                    blank = False,
                    null=True,
                )

    def __str__(self):
        return "{}, {}".format(self.description, self.converter)

    class Meta:
        verbose_name = "DC/DC Converter: Open Loop Transfer Function"
        verbose_name_plural = "DC/DC Converter: Open Loop Transfer Functions"