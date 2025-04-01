from django import template


register = template.Library()


@register.inclusion_tag('collection/components/media-card.html')
def media_card(src='', alt='', num=None, class_list=None):
    return {
        'src': src,
        'alt': alt,
        'num': num,
        'class_list': class_list or []
    }