from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView
from tree.models import Subdivisions, Staff


class SubdivisionsListView(ListView):
    model = Subdivisions
    template_name = "tree/base.html"
    fields = '__all__'


def staff_list_by_division(request, pk):
    if request:
        subdivision = Subdivisions.objects.get(pk=int(pk))
        staff_list = Staff.objects.filter(subdivision=subdivision)
        context = {
            'staff_list': staff_list,
        }
        result = render_to_string('tree/includes/inc_table.html', context)
        return JsonResponse({'result': result})
