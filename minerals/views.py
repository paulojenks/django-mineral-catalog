from django.shortcuts import render, redirect
from django.http import Http404
from . import models


def minerals_list(request, letter=None):
    if not letter:
        minerals = models.Mineral.objects.all().filter(name__istartswith='A')
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
    minerals = models.Mineral.objects.all()
    minerals = minerals.filter(name__contains=term)
    return render(request, 'minerals/index.html', {'minerals': minerals})


def sort_by_letter(request, letter=None):
    minerals = models.Mineral.objects.all()
    if letter is None:
        minerals = minerals.filter(name__startswith='A')
    else:
        minerals = minerals.filter(name__startswith=letter)
    return render(request, 'minerals/index.html', {'minerals': minerals})


def sort_by_group(request, group=None):
    minerals = models.Mineral.objects.all()
    minerals = minerals.filter(group__icontains=group)
    return render(request, 'minerals/index.html', {'minerals': minerals})
