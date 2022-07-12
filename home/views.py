from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from project.models import Project
from home.models import Team
from home.models import Testimony
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    teams = Team.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    testimonys = Testimony.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts, 'projects':projects, 'teams':teams, 'testimonys':testimonys}
    return render(request, 'home.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        #send Email
        send_mail(
            #subject
            'New Message from ' + name,
            #message
            subject,
            #message
            message,
            #from Email
            email,
            #to Email
            [''],
        )
        
        #messages.success(request, 'Your message has been sent!')
        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})

