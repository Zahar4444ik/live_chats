from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, UserUpdateForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'main/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully!!!')
            login(request, user)
            return redirect('rooms')
        else:
            messages.error(request, 'You wrote invalid info!!!')
            return render(request, 'main/register.html', {'form': form})


def sign_in(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'main/login.html', {'form': form})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('rooms')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'main/login.html', {'form': form})


def my_account(request):
    if request.method == 'GET':
        form = UserUpdateForm(instance=request.user)
        return render(request, 'main/my_account.html', {'form': form})
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved successfully.')
            return redirect('rooms')
        else:
            messages.error(request, 'Invalid data')
            return render(request, 'main/my_account.html', {'form': form})

