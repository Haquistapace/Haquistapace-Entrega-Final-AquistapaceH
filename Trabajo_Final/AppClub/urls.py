
from django.urls import path
from AppClub import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('acercademi', views.acercademi, name="acercademi"),
    path('about/', views.about, name="About")
]

# deporte
urlpatterns += [
    path('deporte-list/', views.DeporteListView.as_view(), name="DeporteList"),
    path('deporte-detail/<int:pk>/', views.DeporteDetailView.as_view(), name="DeporteDetail"),
    path('deporte-create/', views.DeporteCreateView.as_view(), name="DeporteCreate"),
    path('deporte-update/<int:pk>/', views.DeporteUpdateView.as_view(), name="DeporteUpdate"),
    path('deporte-delete/<int:pk>/', views.DeporteDeleteView.as_view(), name="DeporteDelete"),
]

# socio
urlpatterns += [
    path('socio-list/', views.SocioListView.as_view(), name="SocioList"),
    path('socio-detail/<int:pk>/', views.SocioDetailView.as_view(), name="SocioDetail"),
    path('socio-create/', views.SocioCreateView.as_view(), name="SocioCreate"),
    path('socio-update/<int:pk>/', views.SocioUpdateView.as_view(), name="SocioUpdate"),
    path('socio-delete/<int:pk>/', views.SocioDeleteView.as_view(), name="SocioDelete"),
]

