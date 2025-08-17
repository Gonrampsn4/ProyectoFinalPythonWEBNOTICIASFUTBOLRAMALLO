
from django.apps import AppConfig

class LeaguesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leagues'

    def ready(self):
        # Post-migrate hook to ensure default leagues exist
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver
        from .models import League

        @receiver(post_migrate, sender=self)
        def create_default_leagues(sender, **kwargs):
            defaults = ["Premier League (ENG)", "Liga Española (ESP)", "Serie A (ITA)"]
            for nm in defaults:
                League.objects.get_or_create(name=nm)
