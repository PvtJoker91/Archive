from django import template
from ad.models import *

register = template.Library()


@register.simple_tag()
def get_clients():
    return Client.objects.all()



