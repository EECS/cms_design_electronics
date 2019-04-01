from django import forms
from django.db import models

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from ..streams import blocks
from ..snippets import snippets

DCDC_CURRENT_TYPE = (
    ("ccm", "Continuous Conduction Mode"),
    ("dcm", "Discontinuous Conduction Mode"),
)

class DcdcPage(Page):
    """DC/DC Converter page model."""

    template = "dcdc/dcdc_page.html"

    design_description = StreamField([
        ("description", blocks.RichtextBlock()),
    ], null=True, blank=False, verbose_name="Design Description")
    
    design_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Circuit Image",
    )

    dcdc_type = models.CharField(
        max_length=75, 
        choices=DCDC_CURRENT_TYPE, 
        blank=False, 
        null=True,
        verbose_name="DC/DC Current Type",
    )

    design_params = ParentalManyToManyField(
                            snippets.DCDCDesignParam,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Design Parameters",
    )

    recommended_components = ParentalManyToManyField(
                            snippets.DCDCRecComps,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Recommended Components",
    )

    selected_components = ParentalManyToManyField(
                            snippets.DCDCSelComps,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Selected Components",
    )

    design_equations = ParentalManyToManyField(
                            snippets.DCDCDesignEquations,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Design Equations",
    )

    open_loop_equations = ParentalManyToManyField(
                            snippets.DCDCOpenLoopEquations,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Open Loop Transfer Functions",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                StreamFieldPanel("design_description"),
                ImageChooserPanel("design_image"),
                FieldPanel("dcdc_type"),
            ],
            heading="DC/DC Converter Description",
        ),
        MultiFieldPanel(
            [
                FieldPanel("design_params", widget=forms.CheckboxSelectMultiple),
                FieldPanel("recommended_components", widget=forms.CheckboxSelectMultiple),
                FieldPanel("selected_components", widget=forms.CheckboxSelectMultiple),
            ],
            heading="DC/DC Converter Design Parameters and Components",
        ),
        MultiFieldPanel(
            [
                FieldPanel("design_equations", widget=forms.CheckboxSelectMultiple),
                FieldPanel("open_loop_equations", widget=forms.CheckboxSelectMultiple),
            ],
            heading="DC/DC Converter Open Loop Design Equations",
        ),
    ]

    class Meta:

        verbose_name = "DC/DC Converter Page"
        verbose_name_plural = "DC/DC Converter Pages"