
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from teams.models import Team


class NewsArticle(models.Model):
    # Campos mínimos solicitados: 2 CharField, 1 RichText, 1 Image, 1 Fecha
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=300, blank=True)
    body = RichTextUploadingField()  # texto enriquecido
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)  # fecha
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    teams = models.ManyToManyField(Team, blank=True, related_name='news_articles')

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
