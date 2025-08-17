
# Blog Fútbol Europeo (Django)

Proyecto de práctica en Django con temática de **noticias de fútbol europeo**.



## Cómo correr
```bash
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

Abre: `http://127.0.0.1:8000/`

## Rutas principales
- `/` → Home
- `/about/` → About
- `/accounts/login/` → Login (Django)
- `/accounts/signup/` → Signup
- `/perfil/` → Perfil (editar bio)
- `/pages/` → Lista de páginas (con "Leer más")
- `/pages/crear/` → Crear página (login requerido)
- `/pages/<slug>/` → Detalle
- `/pages/<slug>/editar/` → Editar (login requerido)
- `/pages/<slug>/borrar/` → Borrar (login requerido)
- `/noticias/` → Lista de noticias
- `/equipos/` → Lista de equipos


## Cargar equipos (Premier, La Liga, Serie A)
Opción A — **Fixture**:
```bash
python manage.py loaddata teams/fixtures/teams_europe_2024_25.json
```

Opción B — **Management command** (idempotente):
```bash
python manage.py load_europe_teams
```

En `/equipos/` podés filtrar por liga desde el selector superior.


## Ligas
- Nueva app `leagues` con CRUD de ligas accesible en `/ligas/` (login requerido para crear/editar/borrar).
- `Team` ahora permite asociar una `League` mediante `league_fk` (opcional para mantener compatibilidad con el campo anterior).
- En la lista de equipos se muestra la liga desde `league_fk` si existe.


### Ligas pre-cargadas
Para tener **Premier League (ENG)**, **Liga Española (ESP)** y **Serie A (ITA)** desde el inicio:
- Opción A (fixture):
  ```bash
  python manage.py loaddata leagues/fixtures/default_leagues.json
  ```
- Opción B (management command, idempotente):
  ```bash
  python manage.py load_default_leagues
  ```
