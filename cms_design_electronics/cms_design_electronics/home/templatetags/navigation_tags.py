from django import template

from wagtail.core.models import Page

from cms_design_electronics.home.models import FooterText, Header
import pdb

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return context['request'].site.root_page


def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return (current_page.url_path.startswith(page.url_path) if current_page else False)

@register.inclusion_tag('tags/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ""
    footer_link = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().body
        footer_link = FooterText.objects.first().footer_link

    return {
        'footer_text': footer_text,
        'footer_link': footer_link,
    }

@register.inclusion_tag('blocks/header.html', takes_context=True)
def get_header_text(context):

    if Header.objects.first() is not None:
        site_title_block = Header.objects.first().site_title
        header_links_blocks = Header.objects.first().header_links

        heading_idx = 0
        url_idx = 1

        headings = []
        urls = []

        for block in site_title_block:
            site_heading = block.value[heading_idx].value
            site_url = block.value[url_idx].value
        
        for block in header_links_blocks:
            headings.append(block.value[heading_idx].value)
            urls.append(block.value[url_idx].value)

    return {
        'site_heading': site_heading,
        'site_url': site_url,
        'headings_urls': zip(headings, urls)
    }