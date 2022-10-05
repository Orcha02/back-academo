from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            
            group = Group.objects.get(name='student')
            user.groups.add(group)
            
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration_and_login/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credenciales de acceso inválidas')

    context = {}
    return render(request, 'registration_and_login/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['admin'])
def home(request):
    context = {}
    return render(request, 'registration_and_login/main.html', context)

def userPage(request):
    context = {}
    return render(request, 'registration_and_login/user.html', context)
