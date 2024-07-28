from django.apps import AppConfig


class CrmConfig(AppConfig):
    
    def ready(self):
        import crm.signals
        
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'
    
    
