from django.apps import AppConfig


class TmartProdcutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tmart_Product'
    def ready(self):
        import tmart_Product.signals
