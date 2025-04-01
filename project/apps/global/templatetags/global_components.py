from django import template


register = template.Library()


@register.inclusion_tag('global/components/button.html')
def button(href='', text='', modifiers_list=None, class_list=None):
    return {
        'href': href,
        'text': text,
        'modifiers_list': modifiers_list or [],
        'class_list': class_list or [],
    }