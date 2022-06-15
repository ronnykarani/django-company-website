from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from project.models import Project


# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts, 'projects':projects}
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html', {})

