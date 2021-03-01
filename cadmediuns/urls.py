from django.urls import path

from s2itdrbello.views import cadmediuns_lista, cadmediuns_insert

urlpatterns = [
    path('lista/', cadmediuns_lista, name="cadmediuns_lista"),
    path('insert/', cadmediuns_insert, name="cadmediuns_insert"),
]
