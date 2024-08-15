from django.shortcuts import render
from .models import Deporte
from AppClub.forms import DeporteFormulario, BuscaDeporteForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deporte, Socio
from django.urls import reverse_lazy
from users.models import Imagen

from django.contrib.auth.mixins import LoginRequiredMixin


# FUNCION DE INICIO / INDEX
def inicio(request):
    return render(request, "AppClub/index.html")

def acercademi(request):
    return render(request, "AppClub/acercademi.html")


# FUNCION DE LOG
@login_required
def about(request):
    return render(request, "AppClub/about.html")


#  Deporte
class DeporteListView(LoginRequiredMixin, ListView):
    model = Deporte
    template_name = "AppClub/deporte_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DeporteDetailView(LoginRequiredMixin, DetailView):
    model = Deporte
    template_name = "AppClub/deporte_detail.html"

    

class DeporteCreateView(LoginRequiredMixin, CreateView):
    

    model = Deporte
    template_name = "AppClub/deporte_create.html"
    fields = ["nombre", "dia" , "imagen"]

   
    success_url = reverse_lazy("DeporteList")


class DeporteUpdateView(LoginRequiredMixin, UpdateView):
    model = Deporte
    success_url = reverse_lazy("DeporteList")
    fields = ["nombre", "dia"]
    template_name = "AppClub/deporte_update.html"


class DeporteDeleteView(LoginRequiredMixin, DeleteView):
    model = Deporte
    success_url = reverse_lazy("DeporteList")
    template_name = 'AppClub/deporte_confirm_delete.html'





    


# VISTAS BASADAS EN CLASES - Socio
class SocioListView(LoginRequiredMixin, ListView):
    model = Socio
    template_name = "AppClub/socio_list.html"


class SocioDetailView(LoginRequiredMixin, DetailView):
    model = Socio
    template_name = "AppClub/socio_detail.html"


class SocioCreateView(LoginRequiredMixin, CreateView):

    model = Socio
    template_name = "AppClub/socio_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("SocioList")


class SocioUpdateView(LoginRequiredMixin, UpdateView):
    model = Socio
    success_url = reverse_lazy("SocioList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppClub/socio_update.html"


class SocioDeleteView(LoginRequiredMixin, DeleteView):
    model = Socio
    success_url = reverse_lazy("SocioList")
    template_name = 'AppClub/socio_confirm_delete.html'


