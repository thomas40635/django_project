from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Film(models.Model):
    titre = models.CharField(max_length=50)
    image = models.TextField()
    realisateurs = models.ManyToManyField('Realisateur')
    synospis = models.TextField()
    categories = models.ManyToManyField('Categorie', related_name='c_i_u')
    dateSortie = models.DateField()

    def __str__(self):
        return '{} de {}'.format(
            self.titre if self.titre is not None else '?',
            ', '.join([str(realisateur) for realisateur in self.realisateurs.all()])
        )


class Realisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    biographie = models.TextField()

    def __str__(self):
        return '{} {}'.format(
            self.prenom if self.prenom is not None else '?',
            self.nom if self.nom is not None else '?',
        )


class Commentaire(models.Model):
    note = models.IntegerField()
    description = models.TextField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return 'Commentaire de {} sur {}'.format(
            self.utilisateur,
            self.film
        )


class Categorie(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(
            self.label,
        )
