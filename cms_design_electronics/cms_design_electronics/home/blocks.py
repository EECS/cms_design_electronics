from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class HeaderBlock(blocks.StreamBlock):
    '''
    Defines a custom header block, based upon a stream block, so that
    links can be added to the header as needed.
    '''
    heading = blocks.CharBlock(classname="full title")
    link = blocks.CharBlock(classname="full title")

    class Meta:
        template = 'blocks/header.html'