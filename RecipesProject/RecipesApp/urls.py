from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('newrecipepage/',views.newrecipepage,name='newrecipe'),
    path('Addrecipe/',views.Addrecipe,name='AddRecipe'),
    path('newuser/',views.newuser,name='newuser'),

]