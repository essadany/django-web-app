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
    
    def __str__(self):
        return f"{self.name}"
    
class Listing(models.Model):
    class ListingType(models.TextChoices):
        RECORDS = 'R'
        MERCHANDISE = 'M'
        POSTERS = 'P'
        MISC = 'S'
    
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        null=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )
    type = models.fields.CharField(
        max_length=5,
        choices=ListingType.choices,
    )
    band = models.ForeignKey(
        Band,
        null=True,
        on_delete=models.SET_NULL,
    )
    
    def __str__(self):
        return f"{self.band.name}"
