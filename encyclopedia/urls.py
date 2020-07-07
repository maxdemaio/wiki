from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create", views.create_entry, name="createEntry"),
    path("wiki/<str:entry>", views.view_entry, name="viewEntry"),
    path("wiki/<str:entry>/edit", views.edit_entry, name="editEntry")
]
