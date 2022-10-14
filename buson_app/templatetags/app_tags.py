from django import template


register = template.Library()

@register.simple_tag
def get_route(employee):
    try:
        return str(employee.bus.main_route)
    except:
        return 'Sem linha'


@register.simple_tag
def get_stop(employee):
    try:
        return str(employee.bus_stop.pk)
    except:
        return 'Sem parada'