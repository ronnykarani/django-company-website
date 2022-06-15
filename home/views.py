from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from project.models import Project
from home.models import Team



# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    teams = Team.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts, 'projects':projects, 'teams':teams}
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html', {})

