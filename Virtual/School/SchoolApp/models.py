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
class Session(models.Model):
    title = models.CharField(max_length=9)
    current = models.BooleanField(default=False)
    number = 0
    class Meta:
        ordering = ["-title"]
    def __str__(self):
        return self.title

class Level(models.Model):
    title = models.CharField(max_length=25)
    Years_Of_Completion = models.IntegerField()
    order_of_completion = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Class(models.Model):
    name = models.CharField(max_length=9)
    year_of_graduation = models.IntegerField(default=2023)
    section = models.ForeignKey(Level, on_delete=models.CASCADE)
    level = models.IntegerField()
    def current_class(self):
        session = Session.objects.all().get(current=True)
        year = int(session.title[5:])
        num_of_years_left = self.year_of_graduation - year
        print(num_of_years_left)
        if num_of_years_left >= 0:
            current_level = self.section.Years_Of_Completion - num_of_years_left 
            self.level = current_level
        else:
            next_section = Level.objects.all().get(order_of_completion = (self.section.order_of_completion + 1))
            self.year_of_graduation += next_section.Years_Of_Completion
            self.section = next_section
            self.level = 1
        
    
    def __str__(self):
        return str(self.section) + " " + str(self.level)

    def save(self, *args, **kwargs):
        self.current_class()
        super().save(*args, *kwargs)
    
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
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    

    def __str__(self):
           return self.RegistrationNumber
    
    def has_perm(self, perm, obj=None):
# Simplest possible answer: Yes, always
        return False
    def has_module_perms(self, app_label):

# Simplest possible answer: Yes, always
        return True
    
    



class Course(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Subject"
class StudentResult(models.Model):
    TERMS = [
        ('FIRST TERM', 'FIRST TERM'),
        ('SECOND TERM', 'SECOND TERM'),
        ('THIRD TERM', 'THIRD TERM')
   ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "result")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Level, on_delete=models.CASCADE,  default=1)
    level = models.IntegerField(default=1)
    term = models.CharField(max_length=32, choices=TERMS)
    average = models.FloatField( default=100)
    Position = models.IntegerField( default=100)
    RemarkFromTeacher = models.CharField(default='', max_length=100)
    RemarkFromPrincipal = models.CharField(default = '', max_length=100)
    def __str__(self):
        name = self.student.firstname +' '+ self.session.title + ' ' + self.term + "result"
        return name
    
    def save(self):
        if self.pk:
            a, b = 0,0
            for result in self.result.all():
                a += result.TotalScore
                b += 1
            self.average = a/b
        super().save()
            
        

class Result(models.Model):
    AssessmentScore = models.IntegerField(default=0)
    ExamScore = models.IntegerField(default=0,)
    teacherInCharge = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="_result")
    student_result = models.ForeignKey(StudentResult, on_delete=models.CASCADE, related_name="result")
    TotalScore = models.IntegerField(default=0,editable=False)
    Grade = models.CharField(default="", max_length=1, editable=False)
    def save(self):
        self.TotalScore = self.AssessmentScore + self.ExamScore
        print(self.TotalScore)
        self.Grade = grade(self.TotalScore)
        super().save()

class ResultFile(models.Model):
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="result_file")
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="result_file")



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
