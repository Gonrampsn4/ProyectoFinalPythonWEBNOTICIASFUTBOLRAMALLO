from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
