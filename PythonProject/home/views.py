from django.shortcuts import render,redirect
from home.forms import UserRegisterForm,AddImageForm
from .models import Images
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request,'home/index.html',{})

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('sign_in')
    else:
        form = UserRegisterForm()
    return render(request, 'home/sign_up.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = AddImageForm(request.POST,
                                   request.FILES)
        if p_form.is_valid():
            user_name=request.user.username
            p_form.save()
            messages.success(request, f'Image added successfully!')
            return redirect('profile')

    else:
        p_form = AddImageForm()

    data = Images.objects.all().order_by('image')
    context = {
        'p_form': p_form,
        'data':data
    }

    return render(request, 'home/profile.html', context)
