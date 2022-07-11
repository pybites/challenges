
from django import template
import math

register = template.Library()

@register.filter
def get_index(l, i):
    return l[i]

@register.filter
def get_font_em_ratio(frequency): #1 freq -> 0, infinite -> pi
    return  1/math.log(10, frequency*20)

