from django.shortcuts import render, redirect
from django.contrib.auth import logout
from. import forms
from. import models
from django import forms as FORM
# Create your views here.
def home(request):
    return render(request, 'SchoolApp/index.html', {})

def profile(request):
    return render(request, 'SchoolApp/student_detail.html', {'student': request.user
    })

def log_out(request):
    logout(request)
    return redirect(home)

def result(request):
    Session = set()
    student = request.user
    for result in student.result.all():
        Session.add(result.session)

    if request.method == "POST":
        form = forms.ResultForm(request.POST)
        print("here")
        form.is_valid()
        print(form.cleaned_data)
        if form.is_valid():
            print(True)
            result = form._clean(request.user)
            print("result")
            print(result)
            return render(request, 'SchoolApp/student_result.html', 
            {'student': request.user,
            'forms': forms.ResultForm,
            'result': result,
            'sessions': Session})
    else:
        form = forms.ResultForm()
    return render(request,'SchoolApp/student_result.html',
        {'student': request.user,
        'form': forms.ResultForm,
        'result':None,
        'sessions': Session})