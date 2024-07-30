from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView
from tree.models import Subdivisions, Staff


class SubdivisionsListView(ListView):
    model = Subdivisions
    template_name = "tree/base.html"
    fields = '__all__'


def staff_list_by_division(request, pk, page):
    if request:
        subdivision_id = pk
        staff_list = Staff.objects.filter(subdivision_id=subdivision_id).order_by('name')
        paginator = Paginator(staff_list, 10)

        try:
            staff_list_paginator = paginator.page(int(page))
        except PageNotAnInteger:
            staff_list_paginator = paginator.page(1)
        except EmptyPage:
            staff_list_paginator = paginator.page(paginator.num_pages)

        context = {
            'staff_list': staff_list_paginator,
        }
        result = render_to_string('tree/includes/inc_table.html', context)
        return JsonResponse({'result': result})
