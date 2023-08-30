from django.urls import path

from . import views

urlpatterns = [
    path("", views.cyto, name="cyto"),
    path("school/",views.school_cyto, name="school-cyto"),
    path("star/",views.star_cyto, name="star-cyto"),
]