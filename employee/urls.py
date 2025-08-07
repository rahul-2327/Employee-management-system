from django.urls import path
from employee import views


# url conf. module
urlpatterns = [
  path('home/', view=views.home)  
]
