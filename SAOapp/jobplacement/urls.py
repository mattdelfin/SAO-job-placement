from django.urls import path

from . import views
urlpatterns = [
    path('', views.jobMain, name="home"),
    path('ojthiring/', views.ojthiring, name="ojthiring"),
]
