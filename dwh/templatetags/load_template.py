from django import template
register = template.Library()

@register.inclusion_tag('dashmenu.html')
def dash_menu(countries, situations):
    return {'countries':countries, 'situations':situations}