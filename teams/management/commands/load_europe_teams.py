
from django.core.management.base import BaseCommand
from teams.models import Team

PREMIER = [
    "Arsenal","Aston Villa","AFC Bournemouth","Brentford","Brighton & Hove Albion",
    "Chelsea","Crystal Palace","Everton","Fulham","Ipswich Town","Leicester City",
    "Liverpool","Manchester City","Manchester United","Newcastle United",
    "Nottingham Forest","Southampton","Tottenham Hotspur","West Ham United","Wolverhampton Wanderers",
]
LALIGA = [
    "Deportivo Alavés","Athletic Club","Atlético de Madrid","FC Barcelona","RC Celta",
    "Getafe CF","Girona FC","UD Las Palmas","CD Leganés","RCD Mallorca",
    "CA Osasuna","Rayo Vallecano","Real Betis","Real Madrid","Real Sociedad",
    "Sevilla FC","Valencia CF","Real Valladolid","Villarreal CF","RCD Espanyol",
]
SERIE_A = [
    "Atalanta","Bologna","Cagliari","Como","Empoli","Fiorentina","Genoa",
    "Hellas Verona","Inter","Juventus","Lazio","Lecce","AC Milan","Monza",
    "Napoli","Parma","Roma","Torino","Udinese","Venezia",
]

class Command(BaseCommand):
    help = "Crea/actualiza equipos de Premier League, La Liga y Serie A (temporada 2024-25). Idempotente."

    def handle(self, *args, **options):
        mapping = {
            'premier': PREMIER,
            'laliga': LALIGA,
            'serie_a': SERIE_A,
        }
        created = 0
        updated = 0
        for league, teams in mapping.items():
            for name in teams:
                obj, was_created = Team.objects.update_or_create(
                    name=name,
                    defaults={'league': league},
                )
                if was_created:
                    created += 1
                else:
                    updated += 1
        self.stdout.write(self.style.SUCCESS(f"Equipos procesados. Creados: {created}, Actualizados: {updated}"))
