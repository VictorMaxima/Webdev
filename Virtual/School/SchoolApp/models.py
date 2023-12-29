from . import forms
from django.contrib import admin
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.urls import reverse
from django.utils.text import slugify

def grade(a):
    if a < 40:
        return "F"
    elif a < 50:
        return "E"
    elif a < 60:
        return "D"
    elif a < 70:
        return "C"
    elif a < 80:
        return "B"
    else:
        return "A"
# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=9)
    year_of_graduation = models.IntegerField(default=2023)
    def __str__(self):
        return str(self.year_of_graduation)
    
class Teacher(models.Model):
    pass
class Student(AbstractBaseUser):
    RegistrationNumber = models.CharField(max_length=9, help_text = "Registration Number", unique=True)
    USERNAME_FIELD = 'RegistrationNumber'
    is_staff = False
    picture = models.ImageField(upload_to='student-images')
    firstname = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    middlename = models.CharField(max_length=32, blank=True)
    state_of_origin = models.CharField(max_length=32)
    backend = 'SchoolApp.forms.MyBackend'
    DateOfBirth = models.DateField(default=datetime.datetime.now)
    Year_Of_Graduation = models.ForeignKey(Class, on_delete=models.CASCADE)
    

    def __str__(self):
           return self.RegistrationNumber
    
    def has_perm(self, perm, obj=None):
# Simplest possible answer: Yes, always
        return False
    def has_module_perms(self, app_label):

# Simplest possible answer: Yes, always
        return True
    
    
class Session(models.Model):
    title = models.CharField(max_length=9)
    current = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title
class StudentResult(models.Model):
    TERMS = [
        ('FIRST TERM', 'FIRST TERM'),
        ('SECOND TERM', 'SECOND TERM'),
        ('THIRD TERM', 'THIRD TERM')
   ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "result")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True)
    term = models.CharField(max_length=32, choices=TERMS)
    average = models.IntegerField( default=100)
    Position = models.IntegerField( default=100)
    RemarkFromTeacher = models.CharField(default='', max_length=100)
    RemarkFromPrincipal = models.CharField(default = '', max_length=100)
    def __str__(self):
        name = self.student.firstname +' '+ self.session.title + ' ' + self.term + "result"
        return name
    
    def save(self):
        a, b = 0, 0
        for result in self.result.all():
            a += result.TotalScore
            b += 1
        self.average = a/b
        super().save()

class Result(models.Model):
    #student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='result')
    AssessmentScore = models.IntegerField(default=0)
    ExamScore = models.IntegerField(default=0,)
    teacherInCharge = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subject")
    student_result = models.ForeignKey(StudentResult, on_delete=models.CASCADE, related_name="result")
    TotalScore = models.IntegerField(default=0,editable=False)
    Grade = models.CharField(default="", max_length=1, editable=False)
    def save(self):
        self.TotalScore = self.AssessmentScore + self.ExamScore
        print(self.TotalScore)
        self.Grade = grade(self.TotalScore)
        super().save()



class StudentResultInline(admin.TabularInline):
    model = StudentResult
    show_change_link = True

class StudentAdmin(admin.ModelAdmin):
    inlines = [
StudentResultInline,
]
class ResultInline(admin.TabularInline):
    model = Result
    show_change_link = True

class StudentResultAdmin(admin.ModelAdmin):
    inlines = [
        ResultInline
    ]

class StudentInline(admin.StackedInline):
    model = Student
    show_change_link = True

class SetAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline
    ]
    
class SchoolData(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    excerpt = models.TextField(default='', editable=False, max_length=500)
    slug = models.SlugField(blank=True, default='')
    def __str__(self):
        return self.title
    
    def save(self):
        self.excerpt = self.content[:100]
        self.slug = slugify(self.title)
        super(SchoolData, self).save()

    def get_absolute_url(self): # < here
        return reverse('news', args=[str(self.slug)])

class SchoolImage(models.Model):
    Image = models.ImageField(upload_to="school_data")
    Data = models.ForeignKey(SchoolData, on_delete=models.CASCADE, related_name="image")

class ImageInline(admin.TabularInline):
    model = SchoolImage
    show_change_link = True

class SchoolDataAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
