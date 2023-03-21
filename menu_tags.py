from django import template
from django.db.models import Q
from ..models import MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info.lstrip('/')
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent').order_by('parent__id', 'text')

    def render_menu_item(menu_item):
        children = menu_items.filter(parent=menu_item)
        active = False
        if menu_item.url and (menu_item.url == current_url or menu_item.url == f"/{current_url}" or menu_item.url == request.resolver_match.url_name):
            active = True
        return {
            'menu_item': menu_item,
            'children': [render_menu_item(child) for child in children],
            'active': active,
        }

    top_level_items = [render_menu_item(menu_item) for menu_item in menu_items.filter(parent__isnull=True)]
    context['menu_items'] = top_level_items
    context['menu_name'] = menu_name
    return ''

