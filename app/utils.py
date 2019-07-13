@register.filter(name='fromunix')
def fromunix(value):
    return datetime.datetime.fromtimestamp(int(value))