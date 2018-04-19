import re

from django import template
from django.db.models import get_model

Project = get_model('bns', 'Project')

register = template.Library()

class Project(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        project = Project.objects.filter(is_public=True).all()
        context[self.var_name] = project
        return ''

@register.tag
def get_project(parser, token):
    """
    Gets all the projects.

    Syntax::

        {% get_project as [var_name] %}

    Example usage::

        {% get_project as project_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%s tag requires arguments" % token.contents.split()[0])
    m = re.search(r'(.*?) and (.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return Project(var_name)
