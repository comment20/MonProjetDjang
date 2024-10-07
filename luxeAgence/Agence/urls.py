from django import views
from . import views
from django.urls import path , include

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('note/',views.note,name="note"),
    path('predict/', views.predict_series, name='predict_series'),
    path('resultats/<str:prediction>/', views.resultats_view, name='resultats'),
    
]
