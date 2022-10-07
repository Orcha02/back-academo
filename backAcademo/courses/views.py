from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from courses.models import Courses, Classes
from django.contrib.auth.decorators import login_required
from registration_and_login.decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


@login_required(login_url='login')
def courses(request):
    courses = Courses.objects.all()
    request_user = request.session.get("user")
    return render(
        request, "courses/courses.html", {"courses": courses})


@login_required(login_url='login')
def course_detail(request, id):
    id_course = Courses.objects.get(id=id)
    classes = Classes.objects.filter(course=id_course)
    return render(request, "courses/course_detail.html", {"classes": classes})


@login_required(login_url='login')
def class_(request, id):
    class_ = Classes.objects.get(id=id)
    return render(request, "courses/class.html", {"class": class_})


@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['admin'])
def home(request):
    context = {}
    return render(request, 'courses/courses.html', context)
