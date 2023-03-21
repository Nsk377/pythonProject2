from django.urls import resolve


def active_menu_item(request):
    current_url = request.path_info.lstrip('/')
    resolver_match = resolve(current_url)
    url_name = resolver_match.url_name if resolver_match.url_name else None
    return {
        'active_menu_item': {
            'url': current_url,
            'url_name': url_name,
        }
    }

