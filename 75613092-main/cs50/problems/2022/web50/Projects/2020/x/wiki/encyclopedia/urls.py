from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.get_entries, name="get_entries"),
    path("fetch.<str:searched>/", views.fetch, name="fetch_searched"),
    path("fetch/", views.fetch, name="fetch"),
    path("new/", views.new_page, name="new_page"),
    path('edit/', views.edit, name='edit'),
    path('save/', views.save, name='save'),
    path("rand/", views.rand, name="rand"),
]
