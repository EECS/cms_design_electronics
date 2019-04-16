from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page

from ..dcdc.models import DcdcPage

class DesignCenterPage(Page):
    """Design center page model."""

    template = "design_center/design_center_page.html"
    max_count = 1

    header = models.CharField(max_length=100, blank=False, null=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("header"),
            ],
            heading="Design Center Options",
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        '''Adding custom functionality to context.'''
        context = super().get_context(request, *args, *kwargs)

        #Get all DC/DC pages
        dcdc_pages = DcdcPage.objects.live().public()

        context["dcdc_pages"] = dcdc_pages

        return context

    class Meta:

        verbose_name = "Design Center Page"
        verbose_name_plural = "Design Center Pages"