from django.shortcuts import render

# Create your views here.
from .forms import  CreateUserForm

def registerPage(request):
		context = {}
		return render(request, 'registration_and_login/register.html', context)

def loginPage(request):
		context = {}
		return render(request, 'registration_and_login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
