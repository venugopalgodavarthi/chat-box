from django.urls import path
from authe import views
app_name='authe'

urlpatterns=[
    path('register/', views.register, name="register"),
    path('login/', views.login1, name="login"),
    path('logout/', views.logout1, name="logout"),
    ]