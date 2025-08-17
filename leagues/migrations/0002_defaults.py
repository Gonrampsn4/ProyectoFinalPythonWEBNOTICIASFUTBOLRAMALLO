
from django.db import migrations

def create_defaults(apps, schema_editor):
    League = apps.get_model('leagues', 'League')
    for nm in ["Premier League (ENG)", "Liga Española (ESP)", "Serie A (ITA)"]:
        League.objects.get_or_create(name=nm)

class Migration(migrations.Migration):
    dependencies = [('leagues','0001_initial')]
    operations = [migrations.RunPython(create_defaults, migrations.RunPython.noop)]
