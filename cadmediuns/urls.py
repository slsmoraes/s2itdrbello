from django.urls import path

from s2itdrbello.views import cadmediuns_lista
from s2itdrbello.views import cadmediuns_insert
from s2itdrbello.views import cadmediuns_update
from s2itdrbello.views import cadmediuns_delete



urlpatterns = [
    path('lista/', cadmediuns_lista, name="cadmediuns_lista"),
    path('insert/', cadmediuns_insert, name="cadmediuns_insert"),
    path('update/<int:id>/', cadmediuns_update, name="cadmediuns_update"),
    path('delete/<int:id>/', cadmediuns_delete, name="cadmediuns_delete"),
]
