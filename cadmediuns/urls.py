from django.urls import path
from s2itdrbello.views import cadmediuns

urlpatterns = [
    path('list/', cadmediuns)
]
