from django.contrib.auth.models import Group
from .models import User

GROUP_NAMES = {'Agents' : 'AG', 'Experts' : 'EX', 'Coordinators' : 'TC'}

def empty_permission_groups():
    for group_name in GROUP_NAMES.keys():
        group = Group.objects.get(name=group_name)
        group.user_set.clear()

def assign_permission_groups():
    for group_name in GROUP_NAMES.keys():
        qs = User.objects.filter(employee__position=GROUP_NAMES[group_name])
        group = Group.objects.get(name=group_name)
        group.user_set.add(*qs)
