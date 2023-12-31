from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timezone import now
# from locations.models import Location
from users.models import User
class Aroma(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=500, null=False)
    image = models.TextField(max_length=500, null=False)

    def __str__(self):
        return  self.name
class Effect(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=500, null=False)
    image = models.TextField(max_length=500, null=False)
    def __str__(self):
        return  self.name

class Terpene(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=1500, null=False)
    image = models.TextField(max_length=500, null=False)
    aromas = models.ManyToManyField("terpenes.Aroma",  blank=True)
    effects = models.ManyToManyField("terpenes.Effect", blank=True)
    def __str__(self):
        return f"{self.name}"
    def __str__(self):
        return  self.name


class TerpeneProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    aromas = models.ManyToManyField("terpenes.Aroma", symmetrical=False)
    effects = models.ManyToManyField("terpenes.Effect", symmetrical=False)
    terpenes = models.ManyToManyField("terpenes.Terpene", symmetrical=False)
    def __str__(self):
        return  f"{self.user.username}"