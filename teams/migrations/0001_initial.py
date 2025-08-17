
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [('leagues','0001_initial')]
    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('league', models.CharField(choices=[('premier', 'Premier League'), ('serie_a', 'Serie A'), ('laliga', 'Liga Española'), ('otros', 'Otros')], default='otros', max_length=20)),
                ('crest', models.ImageField(blank=True, null=True, upload_to='team_crests/')),
                ('league_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leagues.league')),
            ],
            options={'ordering': ['name']},
        ),
    ]
