from django import template
from django.utils.safestring import mark_safe
from ..models import Plat

register = template.Library()


@register.simple_tag
def get_plat():
    """
    得到闲置类型下拉框
    """
    plat_list = Plat.objects.all()
    plat_lists = '<select name=job_func>'
    for name in plat_list:
        cron = '<option value =%s > %s </option>' % (name.id, name)
        cron_lists = '%s' % plat_lists + '%s' % cron
    cron_lists = '%s' % plat_lists + '</select>'
    return mark_safe(cron_lists)