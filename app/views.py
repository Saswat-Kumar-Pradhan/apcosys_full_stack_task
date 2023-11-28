from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .forms import RegistrationForm, LoginForm
from .models import User, Admin

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = True
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user is not None:
                if user.active == True:
                    request.session['user_id'] = user.id
                    return redirect('dashboard')
                else:
                    error_message = "You have no access"
            else:
                error_message = "Invalid username or password"
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_dashboard(request):
    return render(request, 'dashboard_user.html')


def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Admin.objects.filter(username=username, password=password).first()
            if user is not None:
                request.session['user_id'] = user.id
                return redirect('admindashboard')
            else:
                error_message = "Invalid username or password"
                return render(request, 'adin_login.htmlm', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard_admin.html', {'users': users})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Logic to handle editing the user data
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Logic to handle deleting the user
    user.delete()
    return redirect('admindashboard')

def disable_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Logic to handle disabling the user access
    user.active = False
    user.save()
    return redirect('admindashboard')

def enable_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Logic to handle disabling the user access
    user.active = True
    user.save()
    return redirect('admindashboard')