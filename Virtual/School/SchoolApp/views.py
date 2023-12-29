from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from. import forms
from. import models
from django import forms as FORM
# Create your views here.
def home(request):
    Data = models.SchoolData.objects.all()
    DATA = Data.reverse()
    Data1 = DATA[0]
    Selected = DATA[1:4]
    print(Selected)
    return render(request, 'SchoolApp/index.html', {"Data": Selected, "Data1": Data1})

def news_list(request):
    Data = models.SchoolData.objects.all()
    return render(request, "SchoolApp/NewsList.html",{"Data": Data})
def about(request):
    about = models.SchoolData.objects.get(title="AboutUs")
    return render(request, "SchoolApp/about.html", {"about": about})
def profile(request):
    return render(request, 'SchoolApp/student_detail.html', {'student': request.user
    })

def log_out(request):
    logout(request)
    return redirect(home)

def news(request, slug=None):
    SchoolData = get_object_or_404(models.SchoolData, slug=slug)
    return render(request, 'SchoolApp/news.html', {'Data':SchoolData})
16
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