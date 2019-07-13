import datetime

from django.template.defaulttags import register


@register.filter(name='fromunix')
def fromunix(value):
    return datetime.datetime.fromtimestamp(int(value))