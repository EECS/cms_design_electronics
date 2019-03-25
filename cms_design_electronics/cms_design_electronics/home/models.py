from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)

from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel

@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in home/templatetags/
    navigation_tags.py
    """
    body = RichTextField()
    footer_link = RichTextField()

    panels = [
        FieldPanel('body'),
        FieldPanel('footer_link')
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'

class HomePage(Page):
    """
    The Home Page. This looks slightly more complicated than it is. You can
    see if you visit your site and edit the homepage that it is split between
    a:
    - Site title
    - A promotional area
    - Moveable featured site sections
    """

    site_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title of the site.'
    )

    # Promo section of the HomePage
    promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Promo image'
    )
    promo_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    promo_text = RichTextField(
        null=True,
        blank=True,
        help_text='Write some promotional copy'
    )

    site_blurb_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the summary of the website.'
    )
    site_blurb = RichTextField(
        null=True,
        blank=True,
        help_text='Text for the summary of the site.'
    )

    # Featured sections on the HomePage
    # You will see on templates/base/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    featured_section_1_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='First featured section for the homepage. Will display up to '
        'three child items.',
        verbose_name='Featured section 1'
    )

    content_panels = Page.content_panels + [
        FieldPanel("site_title", heading="Site Title"),
        MultiFieldPanel([
            ImageChooserPanel('promo_image'),
            FieldPanel('promo_title'),
            FieldPanel('promo_text'),
        ], heading="Promo section"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('site_blurb_title'),
                FieldPanel('site_blurb'),
                ]),
        ], heading="Summary of the website"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('featured_section_1_title'),
                PageChooserPanel('featured_section_1'),
                ]),
        ], heading="Featured homepage sections", classname="collapsible")
    ]

    def __str__(self):
        return self.site_title