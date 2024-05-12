from django.urls import path

from . import views

app_name='jobplacement'
urlpatterns = [
    path('', views.mainpage),
    path('main/', views.jobMain, name="home"),
    path('jobplacement/report/', views.transRep, name="job_trans_rep"),
]
