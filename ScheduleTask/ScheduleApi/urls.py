from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^schedule/$",views.scheduleapi.as_view(),name="schedule"),
    url(r"^ping/$",views.ping.as_view(),name="ping")
]