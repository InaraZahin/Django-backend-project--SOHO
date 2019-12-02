from django.shortcuts import render, redirect

# Create your views here.

from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView, TemplateView

import requests
from django.shortcuts import render, get_object_or_404



from .forms import ContactUsForm




from .models import Home
from .models import Hero
from .models import Abt
from .models import Proc
from .models import Whyus
from .models import Team
from .models import Works
from .models import Testi
from .models import Blog
from .models import Callaction
def index(request):
    home = Home.objects.all().filter(is_published=True)
    hero = Hero.objects.all().filter(is_published=True)
    abt = Abt.objects.all().filter(is_published=True)
    proc = Proc.objects.all().filter(is_published=True)
    whyus = Whyus.objects.all().filter(is_published=True)
    team = Team.objects.all().filter(is_published=True)
    works = Works.objects.all().filter(is_published = True)
    testi = Testi.objects.all().filter(is_published=True)
    blog = Blog.objects.all().filter(is_published=True)
    action = Callaction.objects.all().filter(is_published=True)
    context = {
        'home': home,
        'hero': hero,
        'abt': abt,
        'proc': proc,
        'whyus': whyus,
        'team': team,
        'works': works,
        'testi': testi,
        'blog': blog,
        'action': action,


    }




    return render(request, 'index.html', context)


def new_index(request):


    return render(request, 'chimper/index.html')
def about(request):


    return render(request, 'chimper/about.html')
def blog(request):


    return render(request, 'chimper/blog.html')
def contact(request):


    return render(request, 'chimper/contact.html')
def services(request):


    return render(request, 'chimper/services.html')
def work(request):


    return render(request, 'chimper/work.html')
def worksingle(request):


    return render(request, 'chimper/work-single.html')


class ContactView(TemplateView):
    template_name = "index.html"

    def post(self, request, args, *kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')



        form = ContactUsForm(request.POST or None)

        errors = None
        if form.is_valid():
            form.save()
        return redirect("/")
        if form.errors:
            errors = form.errors
        context = {
        "form": form,
        }

        return redirect('contact')