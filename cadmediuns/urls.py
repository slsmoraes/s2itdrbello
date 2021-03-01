from django.urls import path

from s2itdrbello.views import cadmediuns_lista


urlpatterns = [
    path('lista/', cadmediuns_lista, name="cadmediuns_lista"),

]
