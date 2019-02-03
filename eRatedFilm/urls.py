"""eRatedFilm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from app.views import IndexView, FilmListView, ProfilView, NoteListView, FilmDetailView, \
    FilmListByNameView, FilmListByCategorieView, FilmListByLetterView, LoginView, LogoutView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index_view'),
    path('films/', FilmListView.as_view(), name='film_list'),
    path('profil/', ProfilView.as_view(), name='profil_view'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('film/<int:pk>', FilmDetailView.as_view(), name='film_detail'),
    path('film/by-letter/<slug:letter>', FilmListByLetterView.as_view(), name='film_list_by_letter'),
    path('film/by-letter/', FilmListByLetterView.as_view(), name='film_list_by_letter'),
    path('film/by-categorie/<slug:categorie>', FilmListByCategorieView.as_view(), name='film_list_by_categorie'),
    path('film/by-categorie/', FilmListByCategorieView.as_view(), name='film_list_by_categorie'),
    path('film/by-name', FilmListByNameView.as_view(), name='film_list_by_name'),
    path('connexion/', LoginView.as_view(), name='login_view'),
    path('deconnexion/', LogoutView.as_view(), name='logout_view'),
]

# urlpatterns += i18n_patterns(
#     path('', IndexView.as_view(), name='index_view'),
#     path('films/', FilmListView.as_view(), name='film_list'),
# )