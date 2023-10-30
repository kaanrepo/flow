from django.contrib.auth.models import Group
from .models import User
from rest_framework.response import Response

GROUP_NAMES = {'Agents' : 'AG', 'Experts' : 'EX', 'Coordinators' : 'TC'}

def empty_permission_groups():
    non_existing_groups = []
    for group_name in GROUP_NAMES.keys():
        try:
            group = Group.objects.get(name=group_name)
            group.user_set.clear()
        except Group.DoesNotExist:
            non_existing_groups.append(group_name)
    if len(non_existing_groups)>0:
        return Response({'message': 'Groups reset. Some groups are not existing.'}, status=200)
    return Response({'message': 'Groups reset.'}, status=200)


def assign_permission_groups():
    non_existing_groups = []
    for group_name in GROUP_NAMES.keys():
        try:
            qs = User.objects.filter(employee__position=GROUP_NAMES[group_name])
            group = Group.objects.get(name=group_name)
            group.user_set.add(*qs)
        except Group.DoesNotExist:
            non_existing_groups.append(group_name)
    if len(non_existing_groups)>0:
        return Response({'message': 'Groups assigned. Some groups are not existing.'}, status=200)
    return Response({'message': 'Groups assigned.'}, status=200)

