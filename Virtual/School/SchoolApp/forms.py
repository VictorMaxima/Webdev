from django import forms
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.forms import UsernameField
from . import models

class MyBackend(BaseBackend):
    def authenticate( request, username=None, password=None):
        try:
            user = models.Student.objects.get(RegistrationNumber=username, password=password)
        except models.Student.DoesNotExist:
            return None
        return user

    def get_user(self, student_id):
        try:
            return models.Student.objects.get(pk=student_id)
        except models.Student.DoesNotExist:
            return None

class AuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        strip=False, widget=forms.PasswordInput
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username is not None and password:
            self.Student = MyBackend.authenticate(
                self.request, username=username, password=password
            )
            if self.Student is None:
                raise forms.ValidationError(
                    "Invalid username/password combination"
                )
            logger.info(
                "Authentication successful for username=%s", username
            )
        return self.cleaned_data
    
    def get_user(self):
        return self.Student


class ResultForm(forms.Form):
    TERMS = [
        ('FIRST TERM', 'FIRST TERM'),
        ('SECOND TERM', 'SECOND TERM'),
        ('THIRD TERM', 'THIRD TERM')
   ]
    SESSIONS = [
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026'),
        ('2026/2027', '2026/2027'),
        ('2027/2028', '2027/2028'),
        ('2028/2029', '2028/2029'),
        ('2029/2030', '2029/2030')
    ]
    term = forms.ChoiceField(choices=TERMS, required=True)
    year = forms.ChoiceField(required=True, choices = SESSIONS)
    def _clean(self, student):
        val = self.cleaned_data
        print(val)
        try:
            result = student.result.all().get(term=val["term"], session__title=val['year'])
            print(result)
            return result
        except:
            self.Newerrors = "the result is not available"
            result = None
            print(self.Newerrors)
            return result