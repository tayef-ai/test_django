from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django import forms
from .models import Student
from .forms import StudentForm


def learn_django(request, id):
    ct = {
        'name': 'akon',
        'mark': 53,
        'dt': datetime.datetime.now(),
        'id': id,
        'title': 'django',
    }
    return render(request, 'home.html', ct)

def about(request):
    ct = {
        'title': 'About Us'
    }
    return render(request, 'about.html', ct)

def show(request):
    query = Student.objects.all()
    return render(request, 'show.html', {'data': query})

def inputdata(request):
    if request.method == 'POST':
        sf = StudentForm(request.POST, request.FILES)
        if sf.is_valid():
            nm = sf.cleaned_data['name']
            em = sf.cleaned_data['email']
            im = sf.cleaned_data['image']
            reg = Student(name=nm, email=em, image=im)
            reg.save()
            return redirect("show")
    else:
        sf = StudentForm(label_suffix=' ')
    return render(request, 'insert.html', {'sform': sf})
