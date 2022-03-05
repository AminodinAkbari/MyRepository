from django.apps import AppConfig


class TmartAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tmart_account'
    def ready(self):
        import tmart_account.signals