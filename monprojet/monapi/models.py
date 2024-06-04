from django.db import models

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=100)

    def __repr__(self):
        return f"{self.nom} {self.prenom}"

    def __str__(self):
        return f"L'utilisateur {self.nom} {self.prenom}"
