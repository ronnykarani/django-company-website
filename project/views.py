from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Project

def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'project/project_list.html', {'projects': projects})
