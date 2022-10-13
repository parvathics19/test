from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('aboutus',views.aboutus,name='aboutus')

]
