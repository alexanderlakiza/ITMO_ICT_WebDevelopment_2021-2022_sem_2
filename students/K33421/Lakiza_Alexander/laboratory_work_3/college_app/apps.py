from django.apps import AppConfig


class CollegeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'college_app'

    def ready(self):
        from . import signals
