from django import template

register = template.Library()

@register.filter
def attr(obj, name):
    """
    Usage: {{ obj|attr:"field_name" }}
    Returns attribute by name. Calls 0-arg callables; returns '' if missing.
    """
    if not obj or not name:
        return ""
    try:
        value = getattr(obj, name)
    except Exception:
        return ""
    try:
        if callable(value):
            return value()
    except TypeError:
        pass
    return "" if value is None else value
