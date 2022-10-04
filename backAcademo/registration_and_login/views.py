from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .forms import  CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'registration_and_login/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'registration_and_login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
