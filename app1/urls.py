from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('welcome',views.welcome,name='welcome'),
    path('app2home',views.app2home,name='app2home')

]
