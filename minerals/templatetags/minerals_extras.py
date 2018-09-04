from django import template
from random import randint
from minerals.models import Mineral

register = template.Library()


@register.inclusion_tag('minerals/random_mineral.html')
def random_mineral():
    """Returns random mineral detail page"""
    random_pk = randint(0, Mineral.objects.count())
    minerals = Mineral.objects.get(pk=random_pk)
    return {'minerals':minerals}


@register.filter(name='no_underscores')
def no_underscores(value):
    """Removes underscores from a word"""
    return value.replace("_", " ")


@register.inclusion_tag('minerals/mineral_categories.html')
def mineral_categories():
    categories = [
        'Silicates',
        'Sulfates',
        'Sulfides',
        'Carbonates',
        'Halides',
        'Sulfosalts',
        'Phosphates',
        'Borates',
        'Organic Minerals',
        'Arsenates',
        'Native Elements',
        'Other'
    ]
    return {'categories': categories}
