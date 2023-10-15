from django.urls import path 
from .views import category_list 

app_name = 'category'

urlpatterns = [
    path('',category_list,name='category_list' ),
]