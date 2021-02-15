from django import template
register = template.Library()


@register.filter
def object_text(object):
    if len(object) == 0:
        return "Здесь ничего нет :("

@register.filter
def stars_render(stars):
    if stars != 0:
        return stars*"★"

@register.filter
def cart_representation(products_in_cart):
    return products_in_cart.values()
