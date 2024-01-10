"""
URL configuration for School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SchoolApp import views as sch_views
from SchoolApp import forms 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_title = "School admin"
admin.site.site_header = "School Admin"
admin.site.index_title= "School Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_news/' ,sch_views.news_list, name='news_list'),
    path('accounts/profile/', sch_views.profile, name='profile'),
    path('accounts/logout/', sch_views.log_out, name="logout"),
    path('accounts/results', sch_views.result, name="result"),
    path('about', sch_views.about, name='about'),
    path('news/<slug:slug>/', sch_views.news, name="news"),
    path('login/', auth_views.LoginView.as_view(template_name='SchoolApp/login.html', form_class=forms.AuthenticationForm), name="login"),
    path('', sch_views.home, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
