from django.shortcuts import render, HttpResponse
from .models import Client, Course
from .forms import SignInForm
from datetime import timezone, date


# Create your views here.
def clients(request):
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})

def courses(request):
    courses = Course.objects.all()
    Course.objects.all().delete()
    return render(request, "courses.html", {"courses": courses})

def signins(request):
    clients = Client.objects.all()
    today = date.today()
    weekday = today.strftime("%A")
    weekday_lower = weekday.lower()
    courses = Course.objects.filter(**{weekday_lower: True})
    return render(request, "signins.html", {"clients": clients, "courses": courses})


def processsignin(request):
    context = {}

    form = SignInForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "complete.html", context)


def complete(request):
    pass