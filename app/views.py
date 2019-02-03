import operator
import urllib
from functools import reduce
from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Count, Q

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from app.models import Film, Categorie, Commentaire
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'index.html'


class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'


class ProfilView(TemplateView):
    template_name = 'profil.html'


class NoteListView(ListView):
    model = Commentaire
    template_name = 'note_list.html'


class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'


class FilmListByLetterView(ListView):
    model = Film
    template_name = 'film_list_by_letter.html'

    def get_context_data(self, **kwargs):
        result = super(FilmListByLetterView, self).get_context_data(**kwargs)
        result['letters'] = [chr(a) for a in range(ord('A'), ord('Z') + 1)]
        letter = self.kwargs.get('letter', False)
        if letter is not False:
            result['letter'] = self.kwargs['letter']
        return result

    def get_queryset(self, *args):
        letter = self.kwargs.get('letter', False)
        if letter is not False:
            return Film.objects.filter(
                Q(titre__startswith=self.kwargs['letter']) | Q(titre__startswith=self.kwargs['letter'].upper()))
        else:
            return Film.objects.all()


class FilmListByCategorieView(ListView):
    model = Film
    template_name = 'film_list_by_categorie.html'

    def get_context_data(self, **kwargs):
        result = super(FilmListByCategorieView, self).get_context_data(**kwargs)
        result["categories"] = Categorie.objects.all()
        categorie = self.kwargs.get('categorie', False)
        if categorie is not False:
            result['categorie'] = self.kwargs['categorie']
        return result

    def get_queryset(self):
        categorie = self.kwargs.get('categorie', False)
        if categorie is not False:
            return Film.objects.filter(categories__slug__exact=categorie)
        else:
            return Film.objects.all()


class FilmListByNameView(ListView):
    model = Film
    template_name = 'film_list_by_name.html'

    def get_queryset(self):
        result = super(FilmListByNameView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(titre__icontains=q) for q in query_list))
            )
        return result


class LoginView(TemplateView):
    template_name = 'login_view.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)
