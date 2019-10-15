from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

# do this to add the signals in apps
    def ready(self):
        import users.signals

