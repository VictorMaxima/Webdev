from django.apps import AppConfig


class SchoolappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SchoolApp'
    def ready(self):
        from . import signals