from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(
        max_length=20,
        choices=Genre.choices,
    )
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )
    
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
class Annonce(models.Model):
    title = models.CharField(max_length=100)
