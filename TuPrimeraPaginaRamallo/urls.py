
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from news.views import home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('ligas/', include('leagues.urls')),

        path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
        path('noticias/', include('news.urls')), # listado de noticias
    path('equipos/', include('teams.urls')), # listado de equipos
    path('perfil/', include('profiles.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
