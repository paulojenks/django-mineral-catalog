from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from . import models


def minerals_list(request):
    minerals = models.Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    try:
        mineral = models.Mineral.objects.filter(pk=pk).values('name', 'category', 'formula', 'strunz_classification',
                                                              'crystal_system', 'unit_cell', 'color',
                                                              'crystal_symmetry', 'cleavage', 'mohs_scale_hardness',
                                                              'luster', 'streak', 'diaphaneity', 'optical_properties',
                                                              'refractive_index', 'crystal_habit', 'specific_gravity',
                                                              'image_caption', 'group')
    except models.Mineral.DoesNotExist:
        raise Http404('You were looking for a rock, but you found a hard place.')
    try:
        mineral = mineral[0]
    except IndexError:
        raise Http404('You were looking for a rock, but you found a hard place.')

    return render(request, 'minerals/detail.html', {'mineral': mineral})


def search(request):
    term = request.GET.get('q')
    minerals = models.Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/index.html', {'minerals': minerals})


def sort_by_letter(request, letter=None):
    minerals = models.Mineral.objects.all().filter(name__startswith=letter)
    return render(request, 'minerals/index.html', {'minerals': minerals})


def sort_by_group(request, group=None):
    minerals = models.Mineral.objects.all().filter(group__icontains=group)
    return render(request, 'minerals/index.html', {'minerals': minerals})
