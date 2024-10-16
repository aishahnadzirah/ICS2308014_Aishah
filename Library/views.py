from django.shortcuts import render
from Library.models import Book, Student, Borrowing, Course, Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index (request):
    context = {
        'greeting' : 1,
    }
    return render (request,"index.html",context)

def view(request):
    context = {
        'firstname':'Aishah Nadzirah'
    }
    return render (request,"view.html",context)

def database(request):
    mybooks = Book.objects.all().values()
    mystudent = Student.objects.all().values()
    myborrow = Borrowing.objects.all().values()
    context = {
        'mybooks' : mybooks,
        'mystudent' : mystudent,
        'myborrow' : myborrow,
        }
    return render (request, "database.html",context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data=Course(code=c_code, description=c_desc)
        data.save()
        
        course_data = Course.objects.all().values()
        dict = {
            'message': 'Data Saved',
            'data' : course_data,
        } 

    else:
        dict = {
            'message': 'hello',
        }

    return render (request,"course.html",dict)

def newmentor(request):
    if request.method == 'POST':
        c_id = request.POST['id']
        c_name = request.POST['name']
        c_no = request.POST['no']
        data=Mentor(menid=c_id, menname=c_name, menroomno=c_no)
        data.save()

        mentor_data = Mentor.objects.all().values()
        dict = {
            'message':'Data Saved',
            'data' : mentor_data,
        }

    else:
        dict = {
            'message': '',
        }

    return render (request,"newmentor.html",dict)

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data
    }

    return render (request, "update_course.html", dict)

def save_update_course(request,code):
    c_desc = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()

    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()

    return HttpResponseRedirect(reverse('course'))

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None
        
        context = {
            "data": data
        }

        return render(request, "search_course.html", context)
    
    return render(request, "search_course.html")
