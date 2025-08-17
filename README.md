
# Blog Fútbol Europeo (Django)

Proyecto de práctica en Django con temática de **noticias de fútbol europeo**.

## Requisitos cumplidos
- ✅ Admin con modelos registrados (`Page`, `NewsArticle`, `Team`, `Profile`).
- ✅ Perfiles de usuario (editar bio), registro (`signup`), login/logout.
- ✅ Páginas (app `pages`) con **lista** y **detalle**; en la lista hay botón **"Leer más"** que navega al detalle por la ruta `pages/<slug>/`.
- ✅ Accesos visibles en la **navbar**: Principal, About, Perfil, Logout, Login, Signup, Noticias, Equipos, Paginas.
- ✅ Si no existen páginas: se muestra **"No hay páginas aún."** en el listado.
- ✅ Editar y borrar páginas solo estando **logeado**.
- ✅ Herencia de templates con `templates/base.html`.
- ✅ `about.html` con información: *Gonzalo Ramallo, gestor de sistemas con 12 años de profesión, programador y analista de datos*.
- ✅ **No se incluye la base de datos** (`db.sqlite3`) y está ignorada en `.gitignore`.

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

## Subir a GitHub
1. Crea un repo nuevo en GitHub.
2. En la carpeta del proyecto:
   ```bash
   git init
   git add .
   git commit -m "Entrega blog fútbol europeo (Django)"
   git branch -M main
   git remote add origin <URL_DEL_REPO>
   git push -u origin main
   ```

## Notas
- Si quieres extender a CKEditor o permisos más finos, puedes agregarlo luego.
- Para precargar datos de equipos o noticias, crea fixtures o usa el admin.


## Imágenes y CKEditor
- Este proyecto usa **django-ckeditor** (con uploader) para campos ricos.
- Subidas se guardan en `MEDIA_ROOT` y se sirven en desarrollo con `MEDIA_URL`.
- En formularios con imágenes se usa `enctype="multipart/form-data"` y las vistas reciben `request.FILES`.


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
Luego podés crear más ligas desde `/ligas/`.
