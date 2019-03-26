from django import forms
from django.db import models

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
    )

from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

class DesignCenter(Page):
    '''
    Houses the design that exists in the landing page
    of the design center.
    '''
    design_name = models.CharField(max_length=100)

    content_panels = Page.content_panels + [
        FieldPanel('design_name', classname="full"),
    ]

    def __str__(self):
        return self.design_name

    class Meta:
        verbose_name = "Design Center Design"
        verbose_name_plural = "Design Center Designs"