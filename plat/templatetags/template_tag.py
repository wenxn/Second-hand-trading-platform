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
    plat_lists = '<select class="form-control" name=plat>'
    for name in plat_list:
        plat = '<option value =%s > %s </option>' % (name, name)
        plat_lists = '%s' % plat_lists + '%s' % plat

    plat_list = '%s' % plat_lists + '</select>'
    return mark_safe(plat_list)

@register.simple_tag
def get_plats():
    """
    得到闲置类型下拉框
    """
    plat_list = Plat.objects.all()
    plat_lists = '<select class="form-control" name=plat> <option value =\'\' > 所有类型 </option> '
    for name in plat_list:
        plat = '<option value =%s > %s </option>' % (name, name)
        plat_lists = '%s' % plat_lists + '%s' % plat

    plat_list = '%s' % plat_lists + '</select>'
    return mark_safe(plat_list)