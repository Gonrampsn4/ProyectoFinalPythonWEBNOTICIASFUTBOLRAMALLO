
from django.db import models
from leagues.models import League

class Team(models.Model):
    PREMIER = 'premier'
    SERIE_A = 'serie_a'
    LALIGA = 'laliga'
    OTHER = 'otros'

    LEAGUE_CHOICES = [
        (PREMIER, 'Premier League'),
        (SERIE_A, 'Serie A'),
        (LALIGA, 'Liga Española'),
        (OTHER, 'Otros'),
    ]

    name = models.CharField(max_length=120, unique=True)
    league = models.CharField(max_length=20, choices=LEAGUE_CHOICES, default=OTHER)
    crest = models.ImageField(upload_to='team_crests/', blank=True, null=True)
    league_fk = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.league_fk.name if self.league_fk else self.get_league_display()}"
