from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Student, models.StudentAdmin)
admin.site.register(models.Class,)
admin.site.register(models.Result)
admin.site.register(models.Session)
admin.site.register(models.StudentResult, models.StudentResultAdmin)
admin.site.register(models.Course)
admin.site.register(models.SchoolData, models.SchoolDataAdmin)
admin.site.register(models.SchoolImage)
admin.site.register(models.Level)

