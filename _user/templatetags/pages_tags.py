from django import template

register = template.Library()

__author__ = 'kremerdesign'

@register.render_tag
def page_menu(context, token):
    pass