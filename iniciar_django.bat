@echo off
echo ================================
echo Iniciando entorno Django...
echo ================================
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
pause
