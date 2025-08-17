
from django.core.management.base import BaseCommand
from leagues.models import League

DEFAULTS = [
    "Premier League (ENG)",
    "Liga Española (ESP)",
    "Serie A (ITA)",
]

class Command(BaseCommand):
    help = "Crea las ligas por defecto si no existen (idempotente)."

    def handle(self, *args, **kwargs):
        created = 0
        for name in DEFAULTS:
            _, was_created = League.objects.get_or_create(name=name)
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Ligas por defecto listas. Creadas: {created}, Totales ahora: {League.objects.count()}"))
