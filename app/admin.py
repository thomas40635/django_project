from django.contrib import admin

from app.models import Film, Realisateur, Commentaire, Categorie

admin.site.register(Film)
admin.site.register(Realisateur)
admin.site.register(Commentaire)
admin.site.register(Categorie)
