from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
#from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from ..streams import blocks

class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    site_tagline = models.CharField(max_length=100, blank=False, null=True)
    site_subtagline = RichTextField(features=["bold", "italic"])
    
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField([
        ("cta", blocks.CTABlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("site_tagline"),
                FieldPanel("site_subtagline"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading="Banner Options",
        ),
        StreamFieldPanel("content"),
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    #@route(r'^subscribe/$')
    #def the_subscribe_page(self, request, *args, **kwargs):
    #    context = self.get_context(request, *args, **kwargs)
    #    return render(request, "home/subscribe.html", context)