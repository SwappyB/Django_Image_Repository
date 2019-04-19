from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'home'

    def ready(self):
        import home.signals
