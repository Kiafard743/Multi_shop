from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    """
    Build querystring while preserving existing GET parameters.
    Example:
        {% querystring page=2 %}
    """
    request = context['request']
    query = request.GET.copy()

    for key, value in kwargs.items():
        query[key] = value

    return query.urlencode()
