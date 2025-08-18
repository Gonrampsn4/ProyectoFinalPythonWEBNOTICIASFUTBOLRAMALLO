
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






  ```
