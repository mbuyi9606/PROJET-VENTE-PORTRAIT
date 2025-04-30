from django.db import models

# Create your models here.
class Portrait(models.Model):
    titre = models.CharField("Titre", max_length=100, blank=True)
    description = models.CharField("Déscription", max_length=100, blank=True)
    image = models.ImageField(upload_to="portraits", null=True, blank=True)

    def __str__(self):
        return self.titre